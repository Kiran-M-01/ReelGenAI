#this file will look for new folders inside the user_uploads folder and converts them to reel if they are not already converted
import os
from text_to_audio import text_to_speech_file
import time
import subprocess
from mutagen.mp3 import MP3
import traceback



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



def create_input_file(folder):

    print("\n===== Creating input.txt =====")

    folder_path = os.path.join("user_uploads", folder)

    print("Folder:", folder_path)

    images = []

    for file in os.listdir(folder_path):
        print("Found:", file)

        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            images.append(file)

    print("Images:", images)

    images.sort()

    audio = MP3(os.path.join(folder_path, "audio.mp3"))
    print("Audio Duration:", audio.info.length)

    audio_duration = audio.info.length

    duration = audio_duration / len(images)
    print("Duration per image:", duration)

    with open(os.path.join(folder_path, "input.txt"), "w") as f:

        for image in images:
            f.write(f"file '{image}'\n")
            f.write(f"duration {duration:.2f}\n")

        # FFmpeg concat demuxer requires the last file to be listed again
        f.write(f"file '{images[-1]}'\n")
        print("input.txt created successfully")



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

                start = time.time()     # Start timer

                try:
                    audio_start = time.time()
                    text_to_audio(folder)
                    audio_end = time.time()

                    create_input_file(folder)

                    video_start = time.time()
                    create_reel(folder)
                    video_end = time.time()

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

                    end = time.time()    # End timer

                    generation_time = round(end - start, 2)

                    print("🎉 Reel generated successfully!")
                    print(f"⏱ Generation Time: {generation_time} seconds")
                    print(f"Audio : {audio_end-audio_start:.2f}s")
                    print(f"Video : {video_end-video_start:.2f}s")
                    print(f"Total : {video_end-audio_start:.2f}s")



                except Exception as e:
                    # print(f"Error processing {folder}: {e}")
                    traceback.print_exc()
                
                
        time.sleep(4)

        