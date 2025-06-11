# caption_generator.py
import google.generativeai as genai
import PIL.Image
import cv2
import numpy as np
from typing import List

def generate_caption(base64_frames: List[str], api_key: str) -> str:
    """
    Generates a caption for a video using the Google Gemini Pro Vision API.

    Args:
        base64_frames (List[str]): A list of base64-encoded frames.
        api_key (str): The Google AI API key for authentication.

    Returns:
        str: The generated caption.
        
    Raises:
        Exception: If the API call fails.
    """
    genai.configure(api_key=api_key)

    image_parts = []
    for frame_bytes in base64_frames:
        nparr = np.frombuffer(frame_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            continue
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = PIL.Image.fromarray(img_rgb)
        image_parts.append(image)

    generation_config = {
        "temperature": 0.3,
        "top_p": 1.0,
        "top_k": 40,
        "max_output_tokens": 200,
    }
    
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = """
    You are an expert video analyst. Your task is to analyze these frames from a video and generate a single, descriptive caption that synthesizes the entire action.

    Follow this exact structure in your response:
    1. Style: Begin with "In the style of a [video type]..." (e.g., cooking tutorial, personal vlog, sports broadcast)
    2. Shot Type: Describe the camera work (e.g., this close-up shot, this wide shot)
    3. Subject and Action: State who or what is the main subject and what they are doing
    4. Setting and Context: Briefly describe the environment or context

    Rules:
    - Create a single, cohesive sentence
    - Do not describe individual frames
    - Do not use preambles or conversational phrases
    - Be concise and focus on the most important information

    Example: "In the style of a personal beauty vlog, this close-up shot shows a young woman with dark hair applying eyeshadow with a makeup brush to her right eyelid, looking directly into the camera against a simple, warm-toned wall."

    Now analyze these frames and provide your caption:
    """

    try:
        response = model.generate_content(
            contents=[prompt] + image_parts[:1],
            generation_config=generation_config,
            stream=False
        )
        
        if hasattr(response, 'text'):
            return response.text.strip()
        elif hasattr(response, 'candidates') and response.candidates:
            if hasattr(response.candidates[0].content.parts[0], 'text'):
                return response.candidates[0].content.parts[0].text.strip()
        
        return "Could not generate caption: Unexpected response format"
        
    except Exception as e:
        error_msg = str(e)
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            error_msg += f"\nResponse: {e.response.text}"
        raise Exception(f"Google Gemini API call failed: {error_msg}")