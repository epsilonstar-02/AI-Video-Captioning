import requests
from typing import List

API_URL = "https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf"

def generate_caption(base64_frames: List[str], api_token: str) -> str:
    """
    Generates a caption for a video by sending its frames to the Hugging Face API.

    Args:
        base64_frames (List[str]): A list of base64-encoded frames.
        api_token (str): The Hugging Face API token for authentication.

    Returns:
        str: The generated caption.
        
    Raises:
        ConnectionError: If the API request fails.
    """
    headers = {"Authorization": f"Bearer {api_token}"}
    
    image_placeholders = "".join(["<image>" for _ in base64_frames])
    prompt_text = (
        f"USER: {image_placeholders}These are frames from a single video. "
        "Analyze them as a sequence and generate a single, cohesive caption. "
        "Describe the video's style, subject, main action, and setting. "
        "Do not describe each frame individually. "
        "Provide only the final caption as your response. ASSISTANT:"
    )

    payload = {
        "inputs": prompt_text,
        "parameters": {
            "images": base64_frames,
            "max_new_tokens": 200
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"API request failed: {e}\nResponse: {response.text}")

    result = response.json()
    full_text = result[0].get("generated_text", "")
    caption = full_text.split("ASSISTANT:")[-1].strip()
    
    return caption