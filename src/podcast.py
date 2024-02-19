from news_api_client import *
from audio import *
import os

BING_API_KEY = os.getenv("BING_API_KEY")

class PodcastGenerator:
    # TODO
    AVAILABLE_COUNTRIES = dict()

    def __init__(self,):
        self.news_client = BingNewsClient(BING_API_KEY)
        self.audio = None

        # hols the transcripts
        self.transcripts = dict()

    def create_podcast(self, country_code, q, count, podcast_file_name, debug_mode=False):
        """Creates news podcast according to params.
        Params:
        country: country domain to search the news in (also determines the language)
        q: Search item for podcast, e.g. Economy, Madam Curie
        count : Amount of news to be retrieved
        podcast_file_name : mp3 file to save the podcast in"""

        lang = helpers.get_lang_code_from_country_code(country_code)

        # if the country code is support
        assert lang is not None

        mkt = f"{lang}-{country_code}"

        # fetch articles
        articles = self.news_client.fetch_news_query(query=q, mkt=mkt, lang=lang, count=count)

        # Scraper.load_summaries(articles, lang, debug=debug_mode)

        # create podcast
        self.audio = Audio(articles=articles, query=q, lang=lang, country_code=country_code,
                           output_name=podcast_file_name, debug_mode=debug_mode)
        self.audio.create_audio()

        # save transcript
        self.transcripts[podcast_file_name] = self.audio.get_transcript()

    def get_transcript(self, podcast_file_name):

        if podcast_file_name in self.transcripts:
            return self.transcripts[podcast_file_name]

        else:
            return f"Something is wrong with {podcast_file_name}, transcript is not found"


    def get_tts_text(self):
        return self.audio.get_script()
