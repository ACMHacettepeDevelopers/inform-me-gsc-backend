import newspaper
class Scraper:

    # obtained from newspaper.languages()
    AVAILABLE_LANGUAGES = ["ar", "be", "bg", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "he", "hi", "hr", "hu", "id", "it", "ja", "ko", "lt", "mk", "nb", "nl", "no", "pl", "pt", "ro", "ru", "sl", "sr", "sv", "sw", "th", "tr", "uk", "vi", "zh"]

    @classmethod
    def load_summaries(cls, articles_fetched,language,debug = False,debug_name = None):
        """Gets summaries of articles via scraping and maps to article objects.
        Alters article.summary and article._summary_is_valid
        If not available sets summary to "" and article._summary_is_valid to false"""

        if language not in Scraper.AVAILABLE_LANGUAGES:
            language = "en"

        article_strings = ""

        # find summaries of articles via scraping (if available) and map to them
        for i, article_fetched in enumerate(articles_fetched):
            article = newspaper.Article(article_fetched.URL, language = language, fetch_images=False)

            try:
                # get summary
                article.download()
                article.parse()
                article.nlp()
                summary = article.summary

                # check summary, if valid map to article_fetched
                article_fetched.summary_is_valid =  Scraper.is_a_valid_summary(summary,language)
                if article_fetched.summary_is_valid:
                    article_fetched.summary = summary

                if debug:
                    article_strings += f"{i + 1} - Url:{article_fetched.URL}\n Summary:\n {summary}\n\n"

            # TODO
            except newspaper.ArticleException:
                print(f"url {article_fetched.URL} cant be scraped")

        if debug:
            with open(f'{debug_name}.txt', 'w', encoding="utf-8") as f:
                f.write(article_strings)

    @classmethod
    def is_a_valid_summary(cls,summary,language):
        """Returns if given summary is valid according to hard coded rules"""

        if len(summary) <10:
            return False

        if language == "tr":
            # sometimes gets caught into cookies
            if "Çerez" in summary or "çerez" in summary:
                return False