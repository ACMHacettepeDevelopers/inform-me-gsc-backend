from article import Article
from src.scraper import Scraper
from translate import Translator
from news_api_client import BingNewsClient


def get_articles_from_res(res: dict):
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

def get_sites(country, category):
    # TODO
    """Returns site parameter for the request in BingNewsClient"""
    if country == "TR":
        match category:
            case "Ekonomi":
                pass
            case "Politika":
                pass

    pass


def get_lang_code_from_mkt(mkt_code):
    # Extracting the language code
    lang_code = mkt_code.split('-')[0]
    return lang_code


def get_category_translation(country_code, category_to_translate):
    # TODO
    """Returns category in the language of country (declared in the bing API mkt)
    Params:
    category_to_translate should be English
    country code should be uppercase code"""

    mkts = BingNewsClient.MKTS

    lang_to_translate_to = None

    for mkt_code in mkts:
        country_code_parsed = mkt_code.split("-")[1]
        if country_code_parsed == country_code:
            lang_to_translate_to = mkt_code.split("-")[0]

    if lang_to_translate_to:
        translator = Translator(to_lang= lang_to_translate_to)
        return translator.translate(category_to_translate)

    # TODO throw exception
    else:
        return f"Translation of {country_code} is not suppported"