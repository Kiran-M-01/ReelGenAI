from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

from werkzeug.security import generate_password_hash

from database import db
from models import Job
from auth_db import (
    create_users_table,
    create_user,
    get_user_by_email,
    get_user_by_username
)


UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
create_users_table()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reelgen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            return "All fields are required"

        if get_user_by_username(username):
            return "Username already exists"

        if get_user_by_email(email):
            return "Email already registered"

        password_hash = generate_password_hash(password)

        create_user(username, email, password_hash)
        return "Registration Successful"

        # print(username)
        # print(email)
        # print(password_hash)

        # return "Recieved Successfully"




@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")

        job = Job(
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
                file.save(os.path.join(folder_path, filename))
                input_files.append(file.filename)

            #SOMETHINGS MISSING
        
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")



        print("Description saved:", desc)

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

with app.app_context():
    db.create_all()

@app.route("/jobs")
def jobs():

    jobs = Job.query.all()

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
    jobs = Job.query.all()
    return render_template("dashboard.html", jobs=jobs)



if __name__ == "__main__":
    app.run(debug=True)