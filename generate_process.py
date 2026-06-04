#this file will look for new folders inside the user_uploads folder and converts them to reel if they are not already converted
import os
from text_to_audio import text_to_speech_file
import time

def text_to_audio(folder):
    print("TTA - ",folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    # text_to_speech_file(text, folder)

def create_reel(folder):
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

                text_to_audio(folder)
                create_reel(folder)

                with open("done.txt", "a") as f:
                        f.write(folder + "\n")
        time.sleep(4)