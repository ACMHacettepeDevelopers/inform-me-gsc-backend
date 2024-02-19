from datetime import date
from article import Article
from gtts import gTTS
from translation import MyTranslator
import helpers


class Audio:
    # gTTS library adds stops for these chars
    # use in between news to add a break
    gTTS_pause = "\n\n\n\n. "

    # add to appropriate places to eliminate the chance of stop in between sentences
    gTTS_break_token = ". "

    def __init__(self, articles: list, query, country_code, lang, output_name, debug_mode=False):

        """create audio object from ISO 361-1 lang code"""

        self._articles = articles
        self._lang = lang

        self.str_date_today = date.today().strftime('%B %d, %Y')  # Format the date as a readable string
        self.str_article_skip = 'Details are at '
        self.str_new_article = "Now we are heading to the next news."
        self.str_not_found = "Sorry, no news or articles were found."
        self.str_news_end = "These were the news."
        self.str_unkown_source = "Sorry, no source were found."
        self.str_news_end = "We've come to the end, thank you for listening."

        country_name = helpers.get_country_name(country_code=country_code)

        self.str_intro = f"Latest news in {country_name} about {query}"
        self.OUTPUT_NAME = output_name

        self._transcript = ""

        # if lang is not english, need to translate these
        if lang != "en":
            self._translator = MyTranslator(to_lang=lang, debug=debug_mode)
            self.str_article_skip = self._translator.translate(self.str_article_skip)
            self.str_new_article = self._translator.translate(self.str_new_article)
            self.str_not_found = self._translator.translate(self.str_not_found)
            self.str_intro = self._translator.translate(self.str_intro)
            self.str_date_today = self._translator.translate(self.str_date_today)
            self.str_unkown_source = self._translator.translate(self.str_unkown_source)
            self.str_news_end = self._translator.translate(self.str_news_end)

        self._article_text = ""

    # @classmethod
    # def from_mkt_code(cls, articles: list, mkt_code: str, intro: str, output_file_name: str, debug_mode):
    #    """create Audio object from ISO 3661 country_code"""
    #
    #    language_code = helpers.get_lang_code_from_mkt(mkt_code)
    #    return cls(articles, language_code, intro, output_file_name, debug_mode=debug_mode)

    def _get_source_to_audit(self, article):
        # return the source to audit
        return article.SOURCE if article.SOURCE else self.str_unkown_source

    def _article_to_text(self, article: Article) -> str:
        """return text of article to audit, return empty text if both description and content is none"""

        text = article.TITLE

        # add title to text
        # text += title + f"{Audio.gTTS_pause}"
        if article.DESCRIPTION is not None:
            text += article.DESCRIPTION

        # TODO
        else:
            pass

        # pause is to create stop in between news
        # token is to eliminate the chance of stops in between sentences
        # text += Audio.gTTS_break_token + self.str_article_skip + Audio.gTTS_break_token + f"{Audio.gTTS_pause}" * 2
        return text

    def create_audio(self):
        """create audio from provided articles"""

        tts = gTTS(text=self.str_not_found, lang=self._lang, tld="com")

        # if no article is found
        if len(self._articles) == 0:
            tts.save(self.OUTPUT_NAME)
            return

        text_articles = self.str_date_today + Audio.gTTS_pause + self.str_intro
        transcript = ""

        for id, article in enumerate(self._articles):

            text_article = self._article_to_text(article)
            transcript += text_article

            source_audit = f"Details are at {self._get_source_to_audit(article)}"

            # add sources
            text_article += source_audit
            transcript += article.URL

            if len(text_article) != 0:
                text_articles += Audio.gTTS_pause + text_article

                # if upcoming article exists, add string_new_article text
                if id != len(self._articles) - 1:
                    # text_articles += self.str_new_article + Audio.gTTS_pause + Audio.gTTS_break_token
                    text_articles += self.str_new_article

                # add ending text
                else:
                    # text_articles += Audio.gTTS_pause + self.str_news_end
                    text_articles += self.str_news_end

        self._transcript = transcript

        self._article_text = text_articles

        tts.text = text_articles
        tts.save(self.OUTPUT_NAME)

    def get_script(self):
        return self._article_text

    def get_transcript(self):
        return self._transcript
