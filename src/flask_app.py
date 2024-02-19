from flask import Flask, send_file, jsonify
from flask import request

import os
from podcast import PodcastGenerator
import helpers

app = Flask(__name__)

podcast_generator = PodcastGenerator()

# Get the service account JSON from the environment variable
service_account_json = os.getenv('SERVICE_ACCOUNT_JSON')


@app.route('/create_podcast')
def create_podcast_route():
    # caching mechanism
    #TODO

    # Get the user's country from the request
    country = request.args.get('country')

    # Get the category from the request
    query = request.args.get('query')

    count = request.args.get("count")

    podcast_file_path = request.args.get("podcast_file_name")

    mode = request.args.get("mode")

    debug = (mode == "debug")

    podcast_generator.create_podcast(country, query, count, podcast_file_path,debug_mode=debug)

    return send_file(podcast_file_path, mimetype='audio/mpeg')


@app.route('/get_transcript')
def get_transcript_route():
    podcast_file_name = request.args.get("podcast_file_name")

    transcript = podcast_generator.get_transcript(podcast_file_name)

    return transcript


@app.route('/create_audio')
def create_audio_route():
    """Sends the audited version of the given parameter text"""
    # TODO
    pass


@app.route('/translate_categories')
def translate_categories_route():
    """Sends the translated version of the given categories in the language of the country
     specified by Bing api"""
    """Categories should have commas in between"""

    category_to_translate = request.args.get("categories_to_translate")
    translation_country_code = request.args.get("translation_country_code")

    mode = request.args.get("mode")

    debug = (mode == "debug")

    translations = helpers.get_category_translation(translation_country_code, category_to_translate,debug_mode=debug)
    # Return a JSON object with the translations
    return jsonify({"translations": translations})


if __name__ == '__main__':
    app.run(debug=False)
