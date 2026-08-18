# 🎬 ReelGenAI

**ReelGenAI** is an AI-powered web application that automatically generates short-form vertical videos (Reels/Shorts) from images and text.

Users can upload multiple images and provide a script or description. The application uses **Amazon Polly** through the **AWS SDK for Python (Boto3)** to convert text into speech. The generated audio duration is analyzed to dynamically synchronize uploaded images, and **FFmpeg** renders the final 1080×1920 vertical video.

The application also includes user authentication, personalized dashboards, job tracking, profile management, user-specific reel galleries, automatic image format conversion, and background reel processing.

---

## ✨ Features

- User registration and login
- Secure password hashing using Werkzeug
- Session-based authentication
- Protected application routes
- Personalized user dashboard
- User profile
- Upload multiple images
- Support for PNG, JPG, JPEG, JFIF, and WebP images
- Automatic JFIF/WebP → JPG conversion
- Cloud-based text-to-speech using Amazon Polly
- AWS integration using Boto3
- Amazon Polly voice support
- Automatic MP3 narration generation
- Dynamic image timing based on narration duration
- Automatic image and audio synchronization
- Background reel processing
- 1080×1920 vertical video generation using FFmpeg
- User-specific reel gallery
- Reel generation job/status tracking
- Responsive web interface

---

# 🚀 Tech Stack

### Backend

- Python
- Flask
- Flask-SQLAlchemy

### Database

- SQLite
- SQLAlchemy
- Raw SQL

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2

### AWS / Cloud

- Amazon Polly
- AWS IAM
- AWS CLI
- Boto3 (AWS SDK for Python)

### AI & Media Processing

- Amazon Polly Text-to-Speech
- FFmpeg
- Mutagen
- Pillow (PIL)

### Authentication & Security

- Werkzeug Password Hashing
- Flask Sessions
- Protected Routes
- AWS IAM Access Control

### Development Tools

- Git
- GitHub
- Python Virtual Environment

---

# 📂 Project Structure

```text
ReelGenAI/
│
├── static/
│   ├── reels/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── create.html
│   ├── gallery.html
│   └── profile.html
│
├── sample_images/
│
├── user_uploads/
│
├── auth_db.py
├── database.py
├── generate_process.py
├── main.py
├── models.py
├── text_to_audio.py
├── requirements.txt
├── .gitignore
└── README.md
```

> Runtime files such as uploaded media, generated reels, local database files, worker state files, Python cache files, and the virtual environment are excluded from Git where applicable.

---

# ⚙️ Workflow

```text
User Visits Landing Page
            │
            ▼
      Register / Login
            │
            ▼
        Dashboard
            │
            ▼
      Create New Reel
            │
            ▼
 Upload Images + Enter Description
            │
            ▼
     Job Added to Database
            │
            ▼
 Background Worker Detects Job
            │
            ▼
 Amazon Polly Generates Narration
        through Boto3
            │
            ▼
      audio.mp3 Generated
            │
            ▼
 Audio Duration Calculated
            │
            ▼
 Image Duration Automatically Calculated
            │
            ▼
 input.txt Generated Dynamically
            │
            ▼
 FFmpeg Combines Images + Audio
            │
            ▼
 1080×1920 Vertical Reel Generated
            │
            ▼
 Gallery + Dashboard Updated
```

---

# ☁️ Amazon Polly Integration

ReelGenAI uses **Amazon Polly** for cloud-based text-to-speech generation.

The Flask application's background worker communicates with Amazon Polly through **Boto3**, the AWS SDK for Python.

The TTS pipeline is:

```text
Text Description
      │
      ▼
Python / Boto3
      │
      ▼
Amazon Polly
      │
      ▼
MP3 Audio Stream
      │
      ▼
audio.mp3
      │
      ▼
Reel Processing Pipeline
```

AWS credentials are configured outside the project using the AWS CLI and are automatically discovered by Boto3.

No AWS credentials are hardcoded in the source code.

---

# 🔐 AWS IAM Configuration

For security, ReelGenAI uses a dedicated **AWS IAM user** for programmatic Amazon Polly access instead of using root account credentials.

The IAM user requires appropriate Amazon Polly permissions.

This keeps AWS authentication separate from the application source code.

> ⚠️ Never commit your AWS Access Key ID or Secret Access Key to GitHub.

---

# 📷 Screenshots

Screenshots can be added for:

- Landing Page
- Login
- Register
- Dashboard
- Create Reel
- Gallery
- Profile

---

# ⚡ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Kiran-M-01/ReelGenAI.git
cd ReelGenAI
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# 🎥 Install FFmpeg

FFmpeg is required for video generation.

Install FFmpeg and make sure it is available in your system PATH.

Verify the installation:

```bash
ffmpeg -version
```

---

# ☁️ AWS Setup

Amazon Polly requires AWS credentials for programmatic access.

## 1. Install AWS CLI

Install the AWS CLI for your operating system.

Verify:

```bash
aws --version
```

## 2. Configure AWS Credentials

Run:

```bash
aws configure
```

Enter your:

```text
AWS Access Key ID
AWS Secret Access Key
Default AWS Region
Default Output Format
```

Example output format:

```text
json
```

The credentials are stored outside the ReelGenAI project and can be automatically discovered by Boto3.

## 3. Verify AWS Authentication

Run:

```bash
aws sts get-caller-identity
```

A successful response confirms that your machine can authenticate with AWS.

> Do not place AWS credentials directly inside `text_to_audio.py`, `.env`, `README.md`, or any file committed to GitHub.

---

# ▶️ Running the Application

ReelGenAI uses two processes:

1. Flask web server
2. Background reel generation worker

## Terminal 1 — Start Flask

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then:

```bash
python main.py
```

## Terminal 2 — Start Background Worker

Open another terminal and activate the same virtual environment:

```bash
venv\Scripts\activate
```

Then:

```bash
python generate_process.py
```

The worker continuously checks for new reel-generation jobs and processes them.

---

# 📝 Usage

1. Open the application in your browser.
2. Register a new account.
3. Login using your credentials.
4. Open the Dashboard.
5. Select **Create Reel**.
6. Upload multiple images.
7. Enter a description or narration script.
8. Submit the reel-generation request.
9. The job is added to the processing queue.
10. Amazon Polly generates the narration.
11. The application calculates the narration duration.
12. Image timing is dynamically calculated.
13. FFmpeg generates the vertical reel.
14. The job status is updated.
15. View the generated reel in your Gallery.

---

# 🧠 Smart Reel Generation

ReelGenAI automatically synchronizes uploaded images with the Amazon Polly-generated narration.

After generating the narration:

1. The application measures the narration duration using Mutagen.
2. It determines the number of uploaded images.
3. It calculates the display duration for each image.
4. A dynamic `input.txt` file is generated.
5. FFmpeg combines the synchronized images and narration.
6. The final video is rendered in vertical 1080×1920 format.

### Example

| Narration Duration | Images Uploaded | Approx. Display Time per Image |
|-------------------:|----------------:|-------------------------------:|
| 20 sec | 10 | 2 sec |
| 45 sec | 15 | 3 sec |
| 60 sec | 20 | 3 sec |
| 90 sec | 30 | 3 sec |

The actual duration is calculated dynamically from:

```text
Image Duration = Narration Duration / Number of Images
```

This allows every uploaded image to appear while keeping the slideshow synchronized with the generated narration.

---

# 🖼️ Automatic Image Format Conversion

ReelGenAI accepts:

```text
PNG
JPG
JPEG
JFIF
WebP
```

JFIF and WebP files are automatically converted to JPG using **Pillow (PIL)** before video processing.

This improves compatibility with the FFmpeg reel-generation pipeline.

---

# 🎙️ Amazon Polly Voice Generation

ReelGenAI currently generates narration using Amazon Polly.

The application communicates with Polly through Boto3:

```python
polly = boto3.client(
    "polly",
    region_name="eu-north-1"
)
```

Speech is generated using:

```python
response = polly.synthesize_speech(
    Text=text,
    OutputFormat="mp3",
    VoiceId="Matthew",
    Engine="standard"
)
```

The voice can currently be changed in the backend by selecting another supported Amazon Polly `VoiceId`.

A user-facing voice selection interface is planned as a future enhancement.

---

# 👤 User Authentication

ReelGenAI includes a custom authentication system.

Authentication features include:

- User registration
- User login
- Password hashing
- Session management
- User logout
- Protected routes
- User-specific application data

Passwords are hashed using Werkzeug before being stored.

Authentication data is handled using SQLite with raw SQL queries.

---

# 📊 Dashboard & Job Tracking

Each authenticated user receives a personalized dashboard.

The dashboard displays the user's reel-generation jobs and their processing status.

Typical job states include:

```text
queued
completed
```

Jobs are associated with individual users so that each user sees their own reel-generation history.

---

# 🎞️ User-Specific Gallery

Generated reels are displayed in the authenticated user's Gallery.

The application retrieves jobs associated with the logged-in user and displays the corresponding generated reel files.

This prevents the Gallery from simply displaying every generated reel to every user.

---

# 📌 Current Features

- ✅ User Registration
- ✅ User Login
- ✅ Password Hashing
- ✅ Session Management
- ✅ Protected Routes
- ✅ User Dashboard
- ✅ User Profile
- ✅ User-Specific Gallery
- ✅ Job Tracking
- ✅ Multiple Image Upload
- ✅ PNG/JPG/JPEG Support
- ✅ JFIF/WebP → JPG Conversion
- ✅ Amazon Polly Text-to-Speech
- ✅ Boto3 AWS Integration
- ✅ AWS IAM Integration
- ✅ MP3 Narration Generation
- ✅ Dynamic Image Timing
- ✅ Automatic Narration Synchronization
- ✅ Dynamic FFmpeg Input Generation
- ✅ FFmpeg Video Rendering
- ✅ 1080×1920 Vertical Video Output
- ✅ Background Reel Processing
- ✅ Responsive UI

---

# 💡 Use Cases

ReelGenAI can be used for:

- Instagram Reels
- YouTube Shorts
- Marketing Content
- Educational Videos
- Product Showcases
- Storytelling
- Social Media Content
- AI-Assisted Content Creation

---

# 🔮 Future Enhancements

- User-selectable Amazon Polly voices
- Download generated reels
- Delete generated reels
- Display reel generation time
- Background music support
- Automatic subtitle generation
- Video transitions and templates
- Real-time processing progress
- Cloud media storage
- Docker deployment
- Email verification
- Admin dashboard

---

# ⚠️ Known Limitations

- FFmpeg must be installed separately.
- AWS credentials and Amazon Polly access are required for text-to-speech generation.
- Generated reels are currently stored locally.
- Uploaded media is currently stored locally.
- Background processing runs as a local Python worker.
- Voice selection is currently configured in the backend rather than through the UI.
- No real-time processing progress indicator is currently available.

---

# 🔒 Security Notes

- Passwords are stored as hashes rather than plain text.
- Authentication uses Flask sessions.
- Protected routes require authentication.
- AWS root credentials are not used by the application.
- AWS credentials are not hardcoded in source code.
- Sensitive/local files are excluded through `.gitignore`.
- AWS IAM is used to control access to Amazon Polly.

---

# 🤝 Contributing

1. Fork the repository.

2. Create a feature branch:

```bash
git checkout -b feature-name
```

3. Commit your changes:

```bash
git commit -m "Add new feature"
```

4. Push to GitHub:

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 👨‍💻 Author

**Kiran M**

GitHub: https://github.com/Kiran-M-01

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub!