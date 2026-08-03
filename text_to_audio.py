import os
import boto3


# Create Amazon Polly client
polly = boto3.client(
    "polly",
    region_name="eu-north-1"
)


def text_to_speech_file(text: str, folder: str) -> str:

    try:
        # Generate speech using Amazon Polly
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna",
            Engine="standard"
        )

    except Exception as e:
        print("\n========== AMAZON POLLY ERROR ==========")
        print(e)
        print("========================================\n")
        return None

    # Path where audio.mp3 will be stored
    save_file_path = os.path.join(
        "user_uploads",
        folder,
        "audio.mp3"
    )

    # Save Polly audio stream to audio.mp3
    with open(save_file_path, "wb") as f:
        f.write(response["AudioStream"].read())

    # Close the AWS response stream
    response["AudioStream"].close()

    print(
        f"{save_file_path}: Amazon Polly audio "
        "generated successfully!"
    )

    return save_file_path