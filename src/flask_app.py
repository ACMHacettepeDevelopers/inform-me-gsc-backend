from io import BytesIO

from flask import Flask, send_file
from flask import request

from src.app import *

app = Flask(__name__)

podcast_generator = PodcastGenerator()

@app.route('/get_podcast')
def get_podcast_route():

    # Get the user's country from the request
    country = request.args.get('country')

    # Get the category from the request
    query = request.args.get('query')

    count = request.args.get("count")

    file_name = request.args.get("file_name")

    podcast_generator.create_podcast(country,query,count,file_name)


    # Return the MP3 data as a response
    # return send_file(BytesIO(f"{file_name}.mp3"), mimetype='audio/mpeg')

@app.route('/get_transcript')
def get_transcript_route():

    podcast_file_name = request.args.get("podcast_file_name")

    transcript = podcast_generator.get_transcript(podcast_file_name)


@app.route('/get_audio')
def get_audio_route():
    """Sends the audited version of the given parameter text"""
    # TODO
    pass

@app.route('/get_category')
def get_category_route():
    """Sends the translated version of the given category """
    # TODO
    pass

if __name__ == '__main__':
    app.run(debug=True)