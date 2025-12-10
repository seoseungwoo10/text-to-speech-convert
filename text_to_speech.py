#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text-to-Speech Conversion using Google Cloud Text-to-Speech API
Reads English text from english.txt and generates an MP3 file with timestamp.
"""

from google.cloud import texttospeech
from datetime import datetime
import os


def synthesize_text_from_file(input_file="english.txt", output_dir="."):
    """
    Synthesizes speech from the input text file.
    
    Args:
        input_file (str): Path to the input text file (default: english.txt)
        output_dir (str): Directory where the output MP3 file will be saved (default: current directory)
    
    Returns:
        str: Path to the generated audio file
    """
    
    # Read text from input file
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f'Error: File "{input_file}" not found.')
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    if not text.strip():
        print("Error: Input file is empty.")
        return None
    
    # Initialize Text-to-Speech client
    try:
        client = texttospeech.TextToSpeechClient()
    except Exception as e:
        print(f"Error initializing Text-to-Speech client: {e}")
        print("Make sure you have set up Google Cloud authentication.")
        return None
    
    # Create input text object
    input_text = texttospeech.SynthesisInput(text=text)
    
    # Configure voice selection
    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().\
    # https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types?hl=ko
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        # name="en-US-Chirp3-HD-Charon",
        name="en-US-Chirp3-HD-Aoede"
    )
    
    # Configure audio encoding
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    # Synthesize speech
    try:
        response = client.synthesize_speech(
            input=input_text,
            voice=voice,
            audio_config=audio_config,
        )
    except Exception as e:
        print(f"Error synthesizing speech: {e}")
        return None
    
    # Generate output filename with timestamp based on input filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Extract filename without extension
    input_filename = os.path.splitext(os.path.basename(input_file))[0]
    output_filename = f"{input_filename}_{timestamp}.mp3"
    output_path = os.path.join(output_dir, output_filename)
    
    # Write audio content to file
    try:
        with open(output_path, "wb") as out:
            out.write(response.audio_content)
        print(f'Audio content written to file "{output_path}"')
        return output_path
    except Exception as e:
        print(f"Error writing audio file: {e}")
        return None


def main():
    """Main function to run the text-to-speech conversion."""
    import sys
    
    print("=" * 60)
    print("Google Cloud Text-to-Speech Converter")
    print("=" * 60)
    
    # Get input file from command line argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "english.txt"
    
    output_dir = "."
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f'Error: File "{input_file}" not found.')
        sys.exit(1)
    
    print(f"Input file: {input_file}")
    
    # Run synthesis
    result = synthesize_text_from_file(input_file, output_dir)
    
    if result:
        print("\nConversion completed successfully!")
        print(f"Output file: {result}")
        sys.exit(0)
    else:
        print("\nConversion failed. Please check the error messages above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
