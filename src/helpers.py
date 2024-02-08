from article import Article

def get_articles_from_res(res:dict):
    articles = list()

    # create articles
    for data in res["value"]:
        title, description, url = data["name"], data["description"], data["url"]
        source, date = data["provider"][0]["name"], data["datePublished"]
        articles.append(Article(title, source, date, url, description))

    return articles