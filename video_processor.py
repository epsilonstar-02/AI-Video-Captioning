import cv2
import base64
from typing import List

def extract_frames(video_path: str, num_frames: int = 8) -> List[str]:
    """
    Extracts a specified number of frames evenly from a video and encodes them in base64.

    Args:
        video_path (str): The path to the video file.
        num_frames (int): The number of frames to extract.

    Returns:
        List[str]: A list of base64-encoded image strings.
        
    Raises:
        IOError: If the video file cannot be opened.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video file: {video_path}")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames < num_frames:
        num_frames = total_frames

    frame_indices = [int(i * total_frames / num_frames) for i in range(num_frames)]
    
    base64_frames = []
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            _, buffer = cv2.imencode(".jpg", frame)
            base64_frame = base64.b64encode(buffer).decode("utf-8")
            base64_frames.append(base64_frame)

    cap.release()
    return base64_frames