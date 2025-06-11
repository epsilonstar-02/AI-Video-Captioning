# main.py
import os
import argparse
from config import GOOGLE_API_KEY
from video_processor import extract_frames
from caption_generator import generate_caption

def process_video(video_path: str):
    """Processes a single video file to generate and print a caption."""
    print("-" * 50)
    print(f"Processing video: {os.path.basename(video_path)}")
    
    try:
        # 1. Extract frames from the video
        image_frames = extract_frames(video_path)
        if not image_frames:
            print("Could not extract frames from the video.")
            return

        # 2. Generate a caption using the AI model
        caption = generate_caption(image_frames, GOOGLE_API_KEY)
        
        # 3. Print the result
        print(f"\n>>> Generated Caption:\n{caption}\n")

    except Exception as e:
        print(f"\n--- An error occurred while processing {os.path.basename(video_path)} ---")
        print(f"Error: {e}")
        print("-" * 50)

def main():
    parser = argparse.ArgumentParser(
        description="Generate captions for video files using Google's Gemini model."
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to a single video file or a directory containing video files."
    )
    args = parser.parse_args()

    # Check for the GOOGLE_API_KEY
    if not GOOGLE_API_KEY:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        print("Please create a .env file and add your key from Google AI Studio.")
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
        print(f"Error: The path '{target_path}' does not exist.")
        return

    if not video_files:
        print("No video files found in the specified path.")
        return

    print(f"Found {len(video_files)} video(s) to process.")
    for video_file in video_files:
        process_video(video_file)

if __name__ == "__main__":
    main()