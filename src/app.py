from config import *
from news_api_client import *
from scraper import *
from audio import *
class PodcastGenerator:

    # TODO
    AVAILABLE_COUNTRIES = dict()

    def __init__(self):
        self.news_client = BingNewsClient(BING_NEWS_API_KEY)
        self.transcript = None
        self.audio = None

    @staticmethod
    def _get_intro_str(country, query):
        return f"Latest news {country} about {query}"

    def create_podcast(self, country, q, count, podcast_file_name, debug_mode=False):
        """Creates news podcast according to params.
        Params:
        country: country domain to search the news in (also determinates the language)
        q: Search item for podcast, e.g Economy, Madam Curie
        count : Amount of news to be retrieved
        podcast_file_name : mp3 file to save the podcast in"""

        lang = ""
        mkt = ""

        # fetch articles
        articles = self.news_client.fetch_news_query(query=q, mkt=mkt, lang=lang, count=count)
        Scraper.load_summaries(articles, lang, debug=debug_mode)

        intro = PodcastGenerator._get_intro_str(country, q)

        self.audio = Audio(articles, lang, intro, podcast_file_name)
        self.audio.create_audio()
        self.transcript = self.audio.get_transcript()

    def get_transcript(self):
        """Returns transcript of the created podcast"""
        return self.transcript
