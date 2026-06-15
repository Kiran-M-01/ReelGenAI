# ReelGenAI 🎬🤖

**ReelGenAI** is an AI-powered web application that automatically generates short-form vertical videos (Reels/Shorts) from images and text. Users can upload images, provide a script or description, and the system converts the text into speech, combines it with the uploaded images, and creates a ready-to-share video reel.

## Features ✨

* Upload multiple images
* Convert text descriptions into speech
* Automatically generate vertical videos (1080×1920)
* Instagram Reels and YouTube Shorts compatible
* Gallery to view generated reels
* Simple and lightweight Flask-based interface
* Automated background processing using FFmpeg

---

## Project Structure 📂

```text
ReelGenAI/
│
├── static/
│   ├── reels/              # Generated reel videos
│   ├── uploads/            # Uploaded images
│   └── css/
│
├── templates/
│   ├── index.html          # Upload page
│   └── gallery.html        # Generated reels gallery
│
├── user_uploads/           # Job folders for processing
│
├── main.py                 # Flask application
├── generate_process.py     # Background reel generation worker
├── text_to_audio.py        # Text-to-speech functionality
├── requirements.txt
└── README.md
```

---

## How It Works ⚙️

```text
User Uploads Images + Text
            │
            ▼
      Flask Web App
            │
            ▼
     Job Folder Created
            │
            ▼
  Background Worker Detects Job
            │
            ▼
     Text → Speech Conversion
            │
            ▼
      Audio File Generated
            │
            ▼
 FFmpeg Combines Images + Audio
            │
            ▼
      Reel Video Generated
            │
            ▼
     Displayed in Gallery
```

---

## Technologies Used 🛠️

* Python
* Flask
* FFmpeg
* HTML5
* CSS3
* Text-to-Speech (TTS)
* JavaScript

---

## Installation 🚀

### 1. Clone the Repository

```bash
git clone https://github.com/Kiran-M-01/ReelGenAI.git
cd ReelGenAI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

Make sure FFmpeg is installed and accessible from your system PATH.

Check installation:

```bash
ffmpeg -version
```

---

## Running the Application ▶️

### Start the Flask Server

```bash
python main.py
```

### Start the Background Processing Worker

Open a second terminal and run:

```bash
python generate_process.py
```

---

## Usage 📸

1. Open the application in your browser.
2. Upload one or more images.
3. Enter a text description or script.
4. Submit the form.
5. Wait for the processing worker to generate the reel.
6. View the generated video in the gallery page.

---

## Example Use Cases 💡

* Instagram Reels creation
* YouTube Shorts generation
* Marketing content
* Educational videos
* Storytelling videos
* Product showcases
* Social media automation

---

## Future Enhancements 🔮

* AI-generated images
* Multiple voice options
* Background music support
* Subtitle generation
* User authentication
* Cloud storage integration
* Video templates
* Real-time processing status
* Docker deployment
* Database support

---

## Known Limitations ⚠️

* Requires FFmpeg installation
* Limited file validation
* No user authentication
* Processing status is not displayed in real time
* Local file storage only

---

## Contributing 🤝

Contributions, bug reports, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## Author 👨‍💻

**Kiran M**

GitHub: [https://github.com/Kiran-M-01](https://github.com/Kiran-M-01)

---

## License 📄

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for educational and personal projects.
