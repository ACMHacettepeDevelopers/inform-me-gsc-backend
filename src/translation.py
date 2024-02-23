from google.cloud import translate_v2 as google_translate
from translate import Translator

import os
# Get the service account JSON from the environment variable
service_account_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
#service_account_json = "service.json"

class MyTranslator:

    def __init__(self, to_lang, debug=False):

        self._debug = debug
        self._to_lang = to_lang

        # use google package
        if not debug:
            self._translate_client = google_translate.Client.from_service_account_json(service_account_json)

        # use 3rd party package
        else:
            self._translate_client = Translator(to_lang=to_lang)

    def translate(self, text):
        """ Target must be an ISO 639-1 language code.
        See https://g.co/cloud/translate/v2/translate-reference#supported_languages """

        # if on debug mode use this library
        if self._debug:
            return self._translate_client.translate(text)

        else:
            result = self._translate_client.translate(text, target_language=self._to_lang)
            return result["translatedText"]