from article import Article
from src.scraper import Scraper


def _get_articles_from_res(res: dict):
    """Returns list of article objects using the given response"""
    articles = list()

    # create articles
    for data in res["value"]:
        title, description, url = data["name"], data["description"], data["url"]
        source, date = data["provider"][0]["name"], data["datePublished"]
        articles.append(Article(title, source, date, url, description))

    return articles


def _get_available_languages():
    return Scraper.AVAILABLE_LANGUAGES


def _get_sites(country, category):
    # TODO
    """Returns site parameter for the request in BingNewsClient"""
    if country == "TR":
        match category:
            case "Ekonomi":
                pass
            case "Politika":
                pass

    pass


def _get_lang_code_from_mkt(mkt_code):
    # Extracting the language code
    lang_code = mkt_code.split('-')[0]
    return lang_code


def get_category_translation(country, category_to_translate):
    # TODO
    """Returns category label for the front end
    Params:
    category_to_translate should be English"""
    pass
