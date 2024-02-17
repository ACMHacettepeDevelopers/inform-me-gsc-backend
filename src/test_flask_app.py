import os

from flask_app import app
from podcast import PodcastGenerator
import json

from pydub import AudioSegment


#def test_translate_category():
#    with app.test_client() as client:
#        # Define the parameters for the request
#        category_to_translate = "sports"
#        translation_country_code = "TR"
#
#        # Make a GET request to the route
#        response = client.get('/translate_category', query_string={
#            'category_to_translate': category_to_translate,
#            'translation_country_code': translation_country_code
#        })
#
#        # Check the response status code
#        assert response.status_code == 200
#
#        # Parse the response data as JSON
#        data = json.loads(response.data.decode('utf-8'))
#
#        # Check if the translation is correct
#        assert 'translated_category' in data
#        print(data["translated_category"])

def test_create_podcast():
    with app.test_client() as client:
        # Make a request to the route
        response = client.get('/create_podcast', query_string={
            'country': 'US',
            'query': 'sports',
            'count': '10',
            'podcast_file_name': 'test.mp3',
            'mode':'debug'
        })

        # Check the response status code
        assert response.status_code == 200

        local_file_name = "test_local"
        local_file_path = f"{local_file_name}.mp3"
        local_file_wav = f"{local_file_name}.wav"

        # Write the bytes to an MP3 file
        with open(local_file_path, 'wb') as f:
            f.write(response.data)

        # Check the content length header
        content_length = int(response.headers['Content-Length'])


        # Load the MP3 file and play it (assuming you have a player installed)
        audio = AudioSegment.from_file(local_file_path, format='mp3')
        audio.export(local_file_wav, format='wav')
        #os.system('start test.wav')  # Open the audio file (Windows)

        ### Clean up the temporary files
        ##os.remove('test.mp3')
        ##os.remove('test.wav')

#def test_podcast_manually():
#    pg = PodcastGenerator()
#    # Get the user's country from the request
#    country = "US"
#
#    # Get the category from the request
#    query = "sports"
#
#    count = 10
#
#    podcast_file_path = "test.mp3"
#
#    mode = "debug"
#
#    debug = (mode == "debug")
#
#    pg.create_podcast(country, query, count, podcast_file_path,debug_mode=debug)

test_create_podcast()