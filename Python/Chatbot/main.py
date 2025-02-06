import pytubefix
import ffmpeg
import openai
import whisper
import sys

# Set your OpenAI API Key (for Mistral)
openai.api_key = "your-openai-api-key"

# Load Whisper model
whisper_model = whisper.load_model("base")

def download_video(url):
    """Download the YouTube video and return the file path."""
    try:
        print("Downloading video...")
        video = pytubefix.Pytube(url)
        video.streams.filter(progressive=True, file_extension='mp4').first().download(output_path="videos")
        print("Video downloaded successfully.")
        return f"videos/{video.title}.mp4"
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

def extract_audio(video_file):
    """Extract audio from the downloaded video file."""
    try:
        print("Extracting audio from video...")
        audio_file = f"{video_file.split('.')[0]}.mp3"
        ffmpeg.input(video_file).output(audio_file).run()
        print("Audio extracted successfully.")
        return audio_file
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None

def transcribe_audio(audio_file):
    """Transcribe audio using Whisper."""
    try:
        print("Transcribing audio...")
        result = whisper_model.transcribe(audio_file)
        print("Audio transcription complete.")
        return result['text']
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

def analyze_text_with_mistral(text):
    """Use Mistral (OpenAI) to analyze the transcribed text."""
    try:
        print("Analyzing text using Mistral...")
        response = openai.Completion.create(
            model="mistral",
            prompt=f"Analyze and summarize the following text:\n\n{text}",
            max_tokens=500
        )
        analysis = response.choices[0].text.strip()
        return analysis
    except Exception as e:
        print(f"Error analyzing text with Mistral: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_video.py <video_url>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    video_file = download_video(url)
    if not video_file:
        sys.exit(1)
    
    audio_file = extract_audio(video_file)
    if not audio_file:
        sys.exit(1)
    
    transcribed_text = transcribe_audio(audio_file)
    if not transcribed_text:
        sys.exit(1)
    
    analysis = analyze_text_with_mistral(transcribed_text)
    if analysis:
        print("Analysis Result:\n")
        print(analysis)

if __name__ == "__main__":
    main()
