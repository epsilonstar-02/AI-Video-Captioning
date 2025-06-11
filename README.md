# Automated Video Captioning with Gemini AI

An intelligent video analysis tool that automatically generates structured, descriptive captions for videos using Google's Gemini AI. The system analyzes video frames and produces professional-quality captions following a structured format.

## Features

- 🎥 Process videos and extract key frames
- 🤖 AI-powered caption generation using Google's Gemini 1.5 Flash model
- 📝 Structured caption output with style, shot type, subject, and setting
- 🖼️ Support for multiple video formats (MP4, AVI, MOV)
- ⚡ Fast and efficient processing

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

### Example Output
```
In the style of a how-to instructional video, this low-angle shot shows a young man demonstrating a yo-yo trick outdoors under a tree's shade.
```

## Project Structure

- `main.py` - Main script to process videos
- `caption_generator.py` - Handles AI model interaction and caption generation
- `video_processor.py` - Manages video frame extraction
- `config.py` - Configuration and environment variables
- `requirements.txt` - Project dependencies

## Getting a Google API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Create an API key
4. Add the key to your `.env` file

## Requirements

- Python 3.8+
- OpenCV
- Google Generative AI
- python-dotenv

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Google Gemini AI for the powerful vision-language model
- OpenCV for video processing capabilities
