from flask import Flask, send_file, jsonify
from flask import request
from podcast import PodcastGenerator
from stt import STT

import helpers

podcast_generator = PodcastGenerator()
app = Flask(__name__)

@app.route('/create_podcast')
def create_podcast_route():
    # caching mechanism
    # TODO

    # Get the user's country from the request, it is ALPHA2 code of the country
    country = request.args.get('country')

    # Get the category from the request
    query = request.args.get('query')

    count = request.args.get("count")

    podcast_file_path = request.args.get("podcast_file_name")

    mode = request.args.get("mode")

    debug = (mode == "debug")

    podcast_generator.create_podcast(country, query, count, podcast_file_path, debug_mode=debug)

    return send_file(podcast_file_path, mimetype='audio/mpeg')


@app.route('/get_transcript')
def get_transcript_route():
    podcast_file_name = request.args.get("podcast_file_name")

    transcript = podcast_generator.get_transcript(podcast_file_name)

    return transcript


@app.route('/translate_categories')
def translate_categories_route():
    """Sends the translated version of the given categories in the language of the country
     specified by Bing api"""
    """Categories should have commas in between"""

    category_to_translate = request.args.get("categories_to_translate")
    translation_country_code = request.args.get("translation_country_code")

    mode = request.args.get("mode")

    debug = (mode == "debug")

    translations = helpers.get_category_translations(translation_country_code, category_to_translate, debug_mode=debug)
    # Return a JSON object with the translations
    return jsonify({"translations": translations})

@app.route('/upload_mp3')
def upload_mp3():
    """Uploads the mp3 file in the request to the server
    First call this route to perform STT
    Use user id in podcast_file_name, don't put .mp3 at the end!"""
    """takes base64 version of mp3 in the header"""
    try:
        # Get the content of the MP3 file from the request
        mp3_base_64 = request.headers.get('mp3')

        # Get the user ID (podcast file name) from the request
        file_name = request.args.get("podcast_file_name")

        file_path = file_name + ".mp3"

        # create mp3 from base 64
        STT.create_mp3_from_base64(mp3_base_64,file_path)

        # Respond with a success message
        return jsonify({'message': 'MP3 file uploaded successfully'})
    except Exception as e:
        # If an error occurs, return an error message
        return jsonify({'error on creating mp3 file': str(e)}), 500  # Return a 500 status code for internal server error

@app.route('/speech_to_text')
def speech_to_text_route():
    """Call this after upload/mp3 route to perform STT"""

    # two latter alpha2 country code
    translation_country_code = request.args.get("country_code")

    lang_code = helpers.get_lang_code_from_country_code(translation_country_code)

    # Get the user ID (or podcast file name) from the request to access the
    file_name = request.args.get("podcast_file_name")
    file_path = file_name + ".mp3"

    text = STT.file_to_text(file_path, language_code=lang_code, country_code=translation_country_code)

    # Return a JSON object with the translations
    return jsonify({"text": text})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
