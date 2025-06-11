# video_processor.py
import cv2
from typing import List
import numpy as np

def extract_frames(video_path: str, num_frames: int = 8) -> List[bytes]:
    """
    Extracts a specified number of frames evenly from a video.

    Args:
        video_path (str): The path to the video file.
        num_frames (int): The number of frames to extract.

    Returns:
        List[bytes]: A list of raw image data (as bytes).
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video file: {video_path}")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames < num_frames:
        num_frames = total_frames

    frame_indices = [int(i * total_frames / num_frames) for i in range(num_frames)]
    
    image_frames = []
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            _, buffer = cv2.imencode(".jpg", frame)
            image_frames.append(buffer.tobytes())

    cap.release()
    return image_frames