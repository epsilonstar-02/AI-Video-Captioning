# main.py
import os
import argparse
from config import API_TOKEN
from video_processor import extract_frames
from caption_generator import generate_caption

def process_video(video_path: str):
    print("-" * 50)
    print(f"Processing video: {os.path.basename(video_path)}")
    
    try:
        base64_frames = extract_frames(video_path)
        if not base64_frames:
            print("Could not extract frames from the video.")
            return

        caption = generate_caption(base64_frames, API_TOKEN)
        print(f"\n>>> Generated Caption:\n{caption}\n")

    except Exception as e:
        print(f"\n--- An error occurred while processing {os.path.basename(video_path)} ---")
        print(f"Error: {e}")
        print("-" * 50)

def main():
    parser = argparse.ArgumentParser(
        description="Generate captions for video files using an AI model."
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to a single video file or a directory containing video files."
    )
    args = parser.parse_args()

    if not API_TOKEN:
        print("Error: HUGGING_FACE_API_TOKEN not found in .env file.")
        print("Please create a .env file and add your token.")
        return

    target_path = args.path
    video_files = []

    if os.path.isdir(target_path):
        print(f"Found directory. Looking for video files in: {target_path}")
        for filename in sorted(os.listdir(target_path)):
            if filename.lower().endswith((".mp4", ".mov", ".avi")):
                video_files.append(os.path.join(target_path, filename))
    elif os.path.isfile(target_path):
        video_files.append(target_path)
    else:
        print(f"Error: Path not found - {target_path}")
        return
    
    if not video_files:
        print("No video files found to process.")
        return

    for video_file in video_files:
        process_video(video_file)

if __name__ == "__main__":
    main()