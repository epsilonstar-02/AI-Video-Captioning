# Automated Video Captioning with Gemini AI

An intelligent video analysis tool that automatically generates structured, descriptive captions for videos using Google's Gemini AI. The system analyzes video frames and produces professional-quality captions following a precise, structured format.

## Features

- 🎥 Process videos and extract key frames using OpenCV
- 🤖 AI-powered caption generation with Google's Gemini 1.5 Flash model
- 🎯 Structured caption output with four key components:
  - Video style (e.g., tutorial, vlog, broadcast)
  - Shot type and camera work
  - Main subject and action
  - Environmental context
- 🖼️ Supports multiple video formats (MP4, AVI, MOV, AVI)
- ⚡ Optimized for fast processing with single-frame analysis
- 🔧 Configurable generation parameters (temperature, top_p, top_k)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automated-video-captioning.git
   cd automated-video-captioning
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

### Process a Single Video
```bash
python main.py path/to/your/video.mp4
```

### Process All Videos in a Directory
```bash
python main.py path/to/videos/directory
```

### Example Outputs

**Cooking Video:**
```
In the style of a cooking tutorial, this close-up shot shows a chef's hands dicing vegetables with precision on a wooden cutting board in a well-lit kitchen.
```

**Action Video:**
```
In the style of a sports highlight, this wide-angle shot captures a basketball player making a three-point shot in a crowded indoor stadium.
```

**Educational Content:**
```
In the style of an educational demonstration, this medium shot features an instructor explaining a science experiment at a whiteboard in a classroom setting.
```

## Project Structure

- `main.py` - Main script for video processing and CLI interface
- `caption_generator.py` - Handles AI model interaction and structured caption generation
- `video_processor.py` - Manages video frame extraction and processing
- `config.py` - Manages environment variables and configuration
- `requirements.txt` - Project dependencies
- `.env` - Stores your Google API key (not version controlled)

## Getting a Google API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Create an API key
4. Create a `.env` file in the project root and add:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Requirements

- Python 3.8+
- OpenCV (for video processing)
- Google Generative AI (for Gemini API)
- python-dotenv (for environment variables)
- Pillow (for image handling)

## Configuration

Adjust generation parameters in `caption_generator.py`:
- `temperature`: Controls randomness (0.0-1.0)
- `top_p`: Nucleus sampling parameter (0.0-1.0)
- `top_k`: Limits token selection to top k
- `max_output_tokens`: Maximum length of generated caption

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Google Gemini AI for the powerful vision-language model
- OpenCV for video processing capabilities
