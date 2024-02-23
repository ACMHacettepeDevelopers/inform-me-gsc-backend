class Article:
    def __init__(self, title, source, publish_date, url, description):
        self.TITLE = title
        self.SOURCE = source
        self.PUBLISH_DATE = publish_date
        self.URL = url
        self.DESCRIPTION = description

        self._summary = None
        self._summary_is_valid = False

    def __repr__(self):
        return f"Description:{self.DESCRIPTION} Source:{self.SOURCE} URL:{self.URL}\n"