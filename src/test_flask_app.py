import os

from flask_app import app
import json

from pydub import AudioSegment


def test_translate_category():
    with app.test_client() as client:
        # Define the parameters for the request
        category_to_translate = "sports"
        translation_country_code = "TR"

        # Make a GET request to the route
        response = client.get('/translate_category', query_string={
            'category_to_translate': category_to_translate,
            'translation_country_code': translation_country_code
        })

        # Check the response status code
        assert response.status_code == 200

        # Parse the response data as JSON
        data = json.loads(response.data.decode('utf-8'))

        # Check if the translation is correct
        assert 'translated_category' in data
        print(data["translated_category"])

def test_create_podcast():
    with app.test_client() as client:
        # Make a request to the route
        response = client.get('/create_podcast', query_string={
            'country': 'USA',
            'query': 'example',
            'count': '1',
            'podcast_file_name': 'test.mp3'
        })

        # Check the response status code
        assert response.status_code == 200

        # Write the bytes to an MP3 file
        with open('test.mp3', 'wb') as f:
            f.write(response.data)

        # Load the MP3 file and play it (assuming you have a player installed)
        audio = AudioSegment.from_file('test.mp3', format='mp3')
        audio.export('test.wav', format='wav')
        os.system('start test.wav')  # Open the audio file (Windows)

        ### Clean up the temporary files
        ##os.remove('test.mp3')
        ##os.remove('test.wav')

