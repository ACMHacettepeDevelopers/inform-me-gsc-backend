import newspaper

class Scraper:

    @classmethod
    def load_summaries(cls, articles, country):

        urls = list()

        article_strings = ""

        for article in articles:
            urls.append(article._URL)

        for i, url in enumerate(urls):

            try:
                newspaper_obj = newspaper.article(url)

                summary = newspaper_obj.summary
                text = newspaper_obj.text

                article_strings += f"{i + 1} - Url:{url} Summary:\n {summary}\n Text:\n {text}\n"

            except newspaper.ArticleException:
                print(f"url {url} cant be scraped")

        with open(f'scrape{country}.txt', 'w', encoding="utf-8") as f:
            f.write(article_strings)

    @classmethod
    def load_summaries_AI(cls, articles, country):

        urls = list()

        article_strings = ""

        for article in articles:
            urls.append(article._URL)

        for i, url in enumerate(urls):
            article = newspaper.Article(url)

            try:
                article.download()
                article.parse()
                article.nlp()

                summary = article.summary
                text = article.text

                article_strings += f"AI{i + 1} - Url:{url} Summary:\n {summary}\n Text:\n {text}\n"
            except newspaper.ArticleException:
                print(f"url {url} cant be scraped")

        with open(f'scrapeAI{country}.txt', 'w', encoding="utf-8") as f:
            f.write(article_strings)
