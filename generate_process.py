#this file will look for new folders inside the user_uploads folder and converts them to reel if they are not already converted
import os
from text_to_audio import text_to_speech_file
import time
import subprocess

def text_to_audio(folder):
    print("TTA - ",folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    text_to_speech_file(text, folder)

def create_reel(folder):
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True, check=True)
    print("CR - ",folder)

if __name__ == "__main__":
    while True:
        print("processing queue...")
        with open("done.txt", "r") as f:
            done_folders = f.readlines()

        done_folders = [f.strip() for f in done_folders]

        folders = os.listdir("user_uploads")

        print("Folders:", folders)
        print("Done:", done_folders)

        for folder in folders:
            print("Checking:", folder)

            if(folder not in done_folders):
                print("Processing:", folder)

                try:
                    text_to_audio(folder)
                    create_reel(folder)

                    # update database
                    # add to done.txt

                except Exception as e:
                    print(f"Error processing {folder}: {e}")
                
                from models import Job
                from database import db
                from main import app

                with app.app_context():
                    job = Job.query.filter_by(uuid=folder).first()

                    if job:
                        job.status = "completed"
                        db.session.commit()

                with open("done.txt", "a") as f:
                        f.write(folder + "\n")
        time.sleep(4)

        