# 🎬 ReelGenAI

> **AI-Powered Reel Generation Platform built with Flask, Python,
> FFmpeg, and AI Text-to-Speech.**

ReelGenAI is a full-stack AI-powered web application that automates the
creation of vertical social media reels. Users can securely register,
upload multiple images, enter a text description, and automatically
generate AI-narrated videos optimized for Instagram Reels and YouTube
Shorts.

The application combines Flask, FFmpeg, AI Text-to-Speech, background
processing, authentication, and media management into a complete
SaaS-style platform.

------------------------------------------------------------------------

# ✨ Features

## 🔐 Authentication

-   User Registration
-   User Login
-   Secure Password Hashing
-   Session Management
-   Protected Routes
-   Logout
-   Flash Messages

## 🎬 Reel Generation

-   Upload Multiple Images
-   AI Text-to-Speech Narration
-   Automatic Vertical Reel Generation (1080×1920)
-   FFmpeg Video Rendering
-   Background Processing Worker
-   Automatic Image Format Conversion
    -   JPG
    -   JPEG
    -   PNG
    -   JFIF
    -   WEBP

## 📊 Dashboard

-   User-specific Dashboard
-   Total Jobs
-   Completed Jobs
-   Processing Jobs
-   Queued Jobs
-   Recent Reel Jobs
-   Job Status Tracking

## 🖼 Gallery

-   User-specific Reel Gallery
-   Responsive Video Cards
-   Built-in Video Player
-   Modern UI

## 👤 Profile

-   User Profile
-   Username & Email
-   Secure Account Access

## 🎨 User Interface

-   Responsive Landing Page
-   Modern Dashboard
-   Create Reel Page
-   Gallery
-   Profile
-   Glassmorphism Design
-   Mobile Friendly

------------------------------------------------------------------------

# 🚀 Tech Stack

### Backend

-   Python
-   Flask

### Database

-   SQLite
-   SQLAlchemy
-   Raw SQL (Authentication)

### Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Jinja2

### AI & Media Processing

-   ElevenLabs Text-to-Speech API
-   FFmpeg

### Authentication

-   Werkzeug Password Hashing
-   Flask Sessions

### Tools

-   Git
-   GitHub

------------------------------------------------------------------------

# 📂 Project Structure

``` text
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
├── user_uploads/
├── auth_db.py
├── database.py
├── generate_process.py
├── main.py
├── models.py
├── text_to_audio.py
├── requirements.txt
├── done.txt
└── README.md
```

------------------------------------------------------------------------

# ⚙️ Workflow

``` text
Landing Page
      │
      ▼
Register / Login
      │
      ▼
Dashboard
      │
      ▼
Create Reel
      │
      ▼
Upload Images + Description
      │
      ▼
Background Worker
      │
      ▼
AI Voice Generation
      │
      ▼
FFmpeg Video Rendering
      │
      ▼
Gallery
```

------------------------------------------------------------------------

# 📷 Screenshots

Add screenshots of:

-   Landing Page
-   Login
-   Register
-   Dashboard
-   Create Reel
-   Gallery
-   Profile

------------------------------------------------------------------------

# ⚡ Installation

``` bash
git clone https://github.com/Kiran-M-01/ReelGenAI.git
cd ReelGenAI
```

Create a virtual environment:

``` bash
python -m venv venv
```

Activate it:

**Windows**

``` bash
venv\Scripts\activate
```

**Linux/macOS**

``` bash
source venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Install FFmpeg and ensure it is available in your system PATH.

Verify:

``` bash
ffmpeg -version
```

Add your ElevenLabs API key in your configuration file.

------------------------------------------------------------------------

# ▶️ Running

Start Flask:

``` bash
python main.py
```

Start the background worker in another terminal:

``` bash
python generate_process.py
```

------------------------------------------------------------------------

# 📝 Usage

1.  Register an account.
2.  Login.
3.  Create a new reel.
4.  Upload images.
5.  Enter a description.
6.  Submit.
7.  Wait for processing.
8.  View the generated reel in the Gallery.

------------------------------------------------------------------------

# 📌 Current Features

-   ✅ Authentication
-   ✅ Password Hashing
-   ✅ Session Management
-   ✅ User Dashboard
-   ✅ User Gallery
-   ✅ User Profile
-   ✅ AI Voice Generation
-   ✅ FFmpeg Rendering
-   ✅ Background Processing
-   ✅ Multiple Image Upload
-   ✅ Automatic Image Conversion
-   ✅ Responsive UI

------------------------------------------------------------------------

# 💡 Use Cases

-   Instagram Reels
-   YouTube Shorts
-   Marketing Content
-   Educational Videos
-   Product Showcases
-   Storytelling
-   AI Content Creation

------------------------------------------------------------------------

# 🔮 Future Enhancements

-   Download Reel
-   Delete Reel
-   Reel Generation Time
-   Multiple AI Voices
-   Background Music
-   Subtitle Generation
-   Docker Deployment
-   Cloud Storage
-   Email Verification
-   Admin Dashboard

------------------------------------------------------------------------

# ⚠️ Known Limitations

-   Requires FFmpeg installation.
-   ElevenLabs API key required.
-   Local storage is used for generated reels.
-   Background processing is local.

------------------------------------------------------------------------

# 🤝 Contributing

1.  Fork the repository.
2.  Create a feature branch.

``` bash
git checkout -b feature-name
```

3.  Commit changes.

``` bash
git commit -m "Add new feature"
```

4.  Push to GitHub.

``` bash
git push origin feature-name
```

5.  Open a Pull Request.

------------------------------------------------------------------------

# 👨‍💻 Author

**Kiran M**

GitHub: https://github.com/Kiran-M-01

------------------------------------------------------------------------

# 📜 License

This project is licensed under the MIT License.

------------------------------------------------------------------------

⭐ If you like this project, consider giving it a star on GitHub!
