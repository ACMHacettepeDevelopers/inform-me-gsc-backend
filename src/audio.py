from datetime import date
from article import Article
from translation import MyTranslator
from tts import TTS
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
        self._country_code = country_code
        self.OUTPUT_NAME = output_name
        self._transcript = f"Sorry, no articles were found with query = {query} . Forward this  to admin please"
        self._article_text = f"Sorry, no articles were found with query = {query} . Forward this  to admin please"
        self._debug_mode = debug_mode
        country_name = helpers.get_country_name(country_code=country_code)
        self.str_intro = f"Latest news in {country_name} about {query}"


        # STRINGS
        self.str_date_today = date.today().strftime('%B %d, %Y')  # Format the date as a readable string
        self.str_details = 'Details are at '
        self.str_new_article = "Now we are heading to the next news."
        self.str_not_found = "Sorry, no news or articles were found."
        self.str_news_end = "These were the news."
        self.str_unkown_source = "Sorry, no source were found."
        self.str_news_end = "We've come to the end, thank you for listening."


        # if lang is not english, need to translate these
        if lang != "en":
            self._translator = MyTranslator(to_lang=lang, debug=debug_mode)
            #self.str_article_skip = self._translator.translate(self.str_article_skip)
            self.str_new_article = self._translator.translate(self.str_new_article)
            self.str_not_found = self._translator.translate(self.str_not_found)
            self.str_intro = self._translator.translate(self.str_intro)
            self.str_date_today = self._translator.translate(self.str_date_today)
            self.str_unkown_source = self._translator.translate(self.str_unkown_source)
            self.str_news_end = self._translator.translate(self.str_news_end)
            self.str_details = self._translator.translate(self.str_details)

    def _get_source_to_audit(self, article):
        # return the source to audit
        return article.SOURCE if article.SOURCE else self.str_unkown_source

    def _article_to_text(self, article: Article) -> str:
        """return text of article to audit. Returns Title+Description, return empty text if both description and content is none"""

        if article.TITLE is None:
            return " "
        
        text = article.TITLE + "/n"

        # add title to text
        # text += title + f"{Audio.gTTS_pause}"
        if article.DESCRIPTION is not None:
            text += article.DESCRIPTION

        # TODO
        else:
            text+="Sorry, no description is found for this article"

        
        # token is to eliminate the chance of stops in between sentences
        # text += Audio.gTTS_break_token + self.str_article_skip + Audio.gTTS_break_token + f"{Audio.gTTS_pause}" * 2
        return text

    def create_audio(self):
        """create audio from provided articles"""

        # if no article is found save the not found audio and log error message
        # than return
        if self._articles is None or len(self._articles) == 0:
            TTS.save_audio(debug_mode=self._debug_mode, text=self.str_not_found, lang_code=self._lang,
                           output_file_name=self.OUTPUT_NAME, country_code=self._country_code)

            if self._articles is None:
                print("No articles could be fetched. Something could be wrong with news api")
                return

        # reset after succesfull fetch
        transcript = ""

        # use ssml
        if not self._debug_mode:
            text_articles = "<speak>"
            print("here")
            text_articles = self.str_date_today + TTS.get_ssml_break(6)+self.str_intro + TTS.get_ssml_break(1)

        else:
            text_articles = self.str_date_today + self.str_intro

        for id, article in enumerate(self._articles):
            # get audio script
            script_to_audit = self._article_to_text(article)

            # write transcript
            transcript += script_to_audit
            transcript += self.str_details + ": " + article.URL
            transcript += "/n"

            # add the source to audio
            source_audit = f"Details are at {self._get_source_to_audit(article)}"
            script_to_audit += source_audit


            if len(script_to_audit) != 0:

                if not self._debug_mode:
                    text_articles += TTS.get_ssml_p_break_token(0)

                # text_articles += Audio.gTTS_pause + script_to_audit
                text_articles += script_to_audit

                # if upcoming article exists, add string_new_article text
                if id != len(self._articles) - 1:
                    # text_articles += self.str_new_article + Audio.gTTS_pause + Audio.gTTS_break_token

                    if not self._debug_mode:
                        text_articles += TTS.get_ssml_break(2)
                        text_articles += self.str_new_article
                        text_articles += TTS.get_ssml_p_break_token(1)

                    else:
                        text_articles += self.str_new_article

                # add ending text
                else:

                    if not self._debug_mode:
                        text_articles += TTS.get_ssml_break(2)
                        text_articles += self.str_news_end
                        text_articles += TTS.get_ssml_p_break_token(1)

                    else:
                        # text_articles += Audio.gTTS_pause + self.str_news_end
                        text_articles += self.str_news_end

        # end ssml
        if self._debug_mode:
            text_articles += "</speak>"

        self._transcript = transcript

        TTS.save_audio(debug_mode=self._debug_mode, text=text_articles, lang_code=self._lang,
                       output_file_name=self.OUTPUT_NAME, country_code=self._country_code)

    def get_transcript(self):
        return self._transcript
