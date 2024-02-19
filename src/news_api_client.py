import requests
import helpers


class BingNewsClient:
    MKTS = ["es-AR", "en-AU", "de-AT", "nl-BE", "fr-BE", "pt-BR", "en-CA", "fr-CA", "es-CL", "da-DK", "fi-FI", "fr-FR",
            "de-DE", "zh-HK", "en-IN", "en-ID", "it-IT", "ja-JP", "ko-KR", "en-MY", "es-MX", "nl-NL", "en-NZ"
                                                                                                      "zh-CN", "pl-PL",
            "en-PH", "ru-RU", "en-ZA", "es-ES", "sv-SE", "fr-CH", "de-CH", "zh-TW", "tr-TR", "en-GB",
            "en-US", "es-US"]

    def __init__(self, sub_key: str):
        self._sub_key = sub_key

    """DOES NOT WORK! BING PROBLEM"""

    # def get_top_news_today(self, mkt, count = 10, sort_by = "relevance"):
    #    """"return top news of today"""
    #
    #    return self.get_news_query("", mkt, count, sort_by)

    def fetch_news_query(self, query, mkt, lang, count=15, sort_by="relevance", get_default_sites=False):
        """Returns JSON response of the found news
        params:
        q > 'q=economy", 'q =economy (site:X.com OR site:Y.com)
        get_default_sites > add hard coded sites to gurantee scraping
        sort_by > date | relevance""
        count is in range [10,100]"""

        if get_default_sites:
            query += helpers.get_sites(mkt, query)

        # make request
        # TODO FRESHNESS?
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key": self._sub_key}
        params = {"q": query, "count": count, "mkt": mkt, "setLang": lang, sort_by: "sort_by"}

        try:
            response = requests.get(search_url, headers=headers, params=params)
            response.raise_for_status()
            results = response.json()
            return helpers.get_articles_from_res(results)

        # TODO
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")

    # def fetch_news_topic(self, mkt, topic):
    #    search_url = f"https://api.bing.microsoft.com/v7.0/news"
#
#    headers = {"Ocp-Apim-Subscription-Key": self._sub_key}
#    params = {"mkt": mkt, "category": topic}
#
#    # make request
#    try:
#        response = requests.get(search_url, headers=headers, params=params)
#        response.raise_for_status()
#        results = response.json()
#        return helpers.get_articles_from_res(results)
#
#    # TODO
#    except requests.exceptions.HTTPError as err:
#        print(f"HTTP error occurred: {err}")

# def get_news_trending_topics(self,mkt,sort_by = "relevance"):
#    search_url = "https://api.bing.microsoft.com/v7.0/news/trendingtopics"
#
#    headers = {"Ocp-Apim-Subscription-Key": self._sub_key}
#    params = {"mkt": mkt, "sortBy": sort_by}
#
#    # make request
#    try:
#        response = requests.get(search_url, headers=headers, params=params)
#        response.raise_for_status()
#        results = response.json()
#        print(results["value"][4])
#        #return helpers.get_articles_from_res(results)
#
#    # TODO
#    except requests.exceptions.HTTPError as err:
#        print(f"HTTP error occurred: {err}")
