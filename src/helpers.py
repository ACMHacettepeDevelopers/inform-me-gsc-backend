from article import Article
from src.scraper import Scraper
from translate import Translator


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


def get_available_mkts():
    """From BingNewsClient"""

    return ["es-AR", "en-AU", "de-AT", "nl-BE", "fr-BE", "pt-BR", "en-CA", "fr-CA", "es-CL", "da-DK", "fi-FI", "fr-FR",
            "de-DE", "zh-HK", "en-IN", "en-ID", "it-IT", "ja-JP", "ko-KR", "en-MY", "es-MX", "nl-NL", "en-NZ"
                                                                                                      "zh-CN", "pl-PL",
            "en-PH", "ru-RU", "en-ZA", "es-ES", "sv-SE", "fr-CH", "de-CH", "zh-TW", "tr-TR", "en-GB",
            "en-US", "es-US"]


def get_lang_code_from_country_code(country_code):
    """Returns language of the country_code (declared in the bing API mkt
    returns none if the country_code is not supported
    Paraös:
    country_code uppercase code of the country"""

    lang_code = None
    mkts = get_available_mkts()

    for mkt_code in mkts:
        country_code_parsed = mkt_code.split("-")[1]
        if country_code_parsed == country_code:
            return mkt_code.split("-")[0]

    return lang_code


def get_category_translation(country_code, category_to_translate):
    """Returns category in the language of country (declared in the bing API mkt)
    Params:
    category_to_translate should be English
    country code should be uppercase code"""

    lang_to_translate_to = get_lang_code_from_country_code(country_code)

    if lang_to_translate_to:
        translator = Translator(to_lang=lang_to_translate_to)
        return translator.translate(category_to_translate)

    # TODO throw exception
    else:
        return f"Translation of {country_code} is not suppported"
