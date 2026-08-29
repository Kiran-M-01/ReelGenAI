from flask import Flask, render_template, request, session, redirect, url_for, flash
import uuid
from werkzeug.utils import secure_filename
import os
from PIL import Image

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database import db
from models import Job
from auth_db import User
from config import DATABASE_URL


UPLOAD_FOLDER = 'user_uploads'

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "jfif",
    "webp"
}


app = Flask(__name__)
app.secret_key = "your_secret_key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    if not username or not email or not password:
        flash("All fields are required.", "danger")
        return redirect(url_for("register"))

    existing_username = User.query.filter_by(
        username=username
    ).first()

    if existing_username:
        flash("Username already exists.", "danger")
        return redirect(url_for("register"))

    existing_email = User.query.filter_by(
        email=email
    ).first()

    if existing_email:
        flash("Email already registered.", "danger")
        return redirect(url_for("register"))

    password_hash = generate_password_hash(password)

    user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )

    db.session.add(user)
    db.session.commit()

    flash("Registration successful! Please login.", "success")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user is None:
        flash("Invalid email address.", "danger")
        return redirect(url_for("login"))

    if not check_password_hash(user.password_hash, password):
        flash("Invalid password.", "danger")
        return redirect(url_for("login"))

    session["user_id"] = user.id

    return redirect(url_for("dashboard"))


@app.route("/create", methods=["GET", "POST"])
def create():

    if "user_id" not in session:
        return redirect(url_for("login"))

    myid = uuid.uuid1()

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")

        job = Job(
            user_id=session["user_id"],
            uuid=rec_id,
            description=desc,
            status="queued"
        )

        db.session.add(job)
        db.session.commit()

        input_files = []

        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(folder_path, exist_ok=True)

        # Save description once
        with open(os.path.join(folder_path, "desc.txt"), "w", encoding="utf-8") as f:
            f.write(desc)

        # Save files
        for key, file in request.files.items():
            if file and file.filename:
                filename = secure_filename(file.filename)

                extension = filename.rsplit(".", 1)[1].lower()

                save_path = os.path.join(folder_path, filename)

                file.save(save_path)

                if extension in ["jfif", "webp"]:

                    new_filename = filename.rsplit(".", 1)[0] + ".jpg"

                    new_path = os.path.join(folder_path, new_filename)

                    image = Image.open(save_path).convert("RGB")
                    image.save(new_path, "JPEG")

                    os.remove(save_path)

                    input_files.append(new_filename)

                else:

                    input_files.append(filename)

            #SOMETHINGS MISSING
        
        # for fl in input_files:
        #     with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
        #         f.write(f"file '{fl}'\nduration 2\n")



        print("Description saved:", desc)

    return render_template("create.html", myid=myid)



@app.route("/gallery")
def gallery():

    if "user_id" not in session:
        return redirect(url_for("login"))
    
    jobs = Job.query.filter_by(
        user_id = session["user_id"]
    ).all()

    reels = []
    for job in jobs:

        filename = job.uuid + ".mp4"

        if os.path.exists(os.path.join("static", "reels", filename)):
            reels.append(filename)

    
    return render_template("gallery.html", reels=reels)

with app.app_context():
    db.create_all()



@app.route("/jobs")
def jobs():

    if "user_id" not in session:
        return redirect(url_for("login"))

    jobs = Job.query.filter_by(
    user_id=session["user_id"]
    ).all()

    result = []

    for job in jobs:
        result.append({
            "id": job.id,
            "uuid": job.uuid,
            "description": job.description,
            "status": job.status
        })

    return result

@app.route("/dashboard")
def dashboard():

    print(session)

    if "user_id" not in session:
        return redirect(url_for("login"))
    
    jobs = Job.query.filter_by(
    user_id=session["user_id"]
    ).all()

    return render_template("dashboard.html", jobs=jobs)


@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = db.session.get(User, session["user_id"])

    if user is None:
        session.pop("user_id", None)
        return redirect(url_for("login"))

    return render_template("profile.html", user=user)

@app.route("/logout")
def logout():

    session.pop("user_id", None)

    flash("You have been logged out successfully.", "info")

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)