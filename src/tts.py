from gtts import gTTS
from google.cloud import texttospeech
import os

# Get the service account JSON from the environment variable
#service_account_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
service_account_json = "service.json"
class TTS:

    @staticmethod
    def save_audio(debug_mode,text,lang_code,output_file_name,country_code =None):
        if debug_mode:
            tts = gTTS(text=text, lang=lang_code, tld="com")
            tts.save(output_file_name)

        else:
            # TODO ! MUST BE VALID
            mkt_code = lang_code+"-"+country_code

            # Instantiates a client
            client = texttospeech.TextToSpeechClient.from_service_account_json(service_account_json)

            # Set the text input to be synthesized
            synthesis_input = texttospeech.SynthesisInput(text=text)

            # Build the voice request, select the language code ("en-US") and the ssml
            # voice gender ("neutral")
            voice = texttospeech.VoiceSelectionParams(
                language_code=mkt_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
     )

            # Select the type of audio file you want returned
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )

            # Perform the text-to-speech request on the text input with the selected
            # voice parameters and audio file type
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            # The response's audio_content is binary.
            with open(output_file_name, "wb") as out:
                # Write the response to the output file.
                out.write(response.audio_content)
