class Article():

    def __init__(self,title,source,publish_date,url,description):
        self._TITLE = title
        self._SOURCE = source
        self._PUBLISH_DATE = publish_date
        self._URL = url

        self.text = None
        self._description = description
        self._summary = None
        self._summary_is_valid = False

    def __repr__(self):
        return f"Description:{self._description} Source:{self._SOURCE} URL:{self._URL}\n"

    #def __repr__(self):
    #    return f"Title:{self._TITLE}, Description:{self._description}\n,Summary:{self._summary},PublishedAt:{self._PUBLISH_DATE}\n" \
    #           f"Source:{self._SOURCE}"