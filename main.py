from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
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
    return render_template("gallery.html")

app.run(debug=True)