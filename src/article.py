class Article:

    def __init__(self, title, source, publish_date, url, description):
        self.TITLE = title
        self.SOURCE = source
        self.PUBLISH_DATE = publish_date
        self.URL = url

        self._description = description
        self._summary = None
        self._summary_is_valid = False

    def __repr__(self):
        return f"Description:{self._description} Source:{self.SOURCE} URL:{self.URL}\n"

    # def __repr__(self):
    #    return f"Title:{self._TITLE}, Description:{self._description}\n,Summary:{self._summary},PublishedAt:{self._PUBLISH_DATE}\n" \
    #           f"Source:{self._SOURCE}"
