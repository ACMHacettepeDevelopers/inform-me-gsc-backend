from article import Article
from src.scraper import Scraper


def get_articles_from_res(res: dict):
    """Returns list of article objects using the given response"""
    articles = list()

    # create articles
    for data in res["value"]:
        title, description, url = data["name"], data["description"], data["url"]
        source, date = data["provider"][0]["name"], data["datePublished"]
        articles.append(Article(title, source, date, url, description))

    return articles


def get_available_languages():
    return Scraper.AVAILABLE_LANGUAGES


def get_sites(country, category):
    # TODO
    """Returns site parameter for the request in BingNewsClient"""
    pass
