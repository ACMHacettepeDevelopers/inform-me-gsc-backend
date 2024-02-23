from google.cloud import speech_v1p1beta1 as speech

from google.cloud import speech
from google.oauth2 import service_account
import helpers
import base64

import os
# Get the service account JSON from the environment variable
service_account_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
#service_account_json = "service.json"

class STT:

    # string to return if audio can't be processed
    # translated to the specified language
    DEFAULT_STRING = "agenda"

    @staticmethod
    def create_mp3_from_base64(base64_content, output_file_path):
        # Decode the base64 content into binary data
        binary_data = base64.b64decode(base64_content)

        # Write the binary data to a file
        with open(output_file_path, "wb") as output_file:
            output_file.write(binary_data)

    @staticmethod
    def file_to_text(file_path: str,language_code,country_code):
        """Transcribe the given audio file."""
        credentials = service_account.Credentials.from_service_account_file(service_account_json)
        client = speech.SpeechClient(credentials=credentials)

        with open(file_path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=16000,
            language_code=language_code+"-"+country_code
        )

        response = client.recognize(config=config, audio=audio)

        if len(response.results) != 0:
            return response.results[0].alternatives[0].transcript

        else:
            return helpers.get_category_translations(country_code,STT.DEFAULT_STRING)
