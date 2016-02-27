import requests
from constant import *
import logging
import bs4


def bs4_decorator(function):
    """
    Decorator
    Generator a soup from give html content
    :param function:
    :return Soup , None:
    """
    def soup_generator(self, url):
        response = function(self, url)
        if response:  # May get a None if requests time out
            return bs4.BeautifulSoup(response.text)
        else:
            return None

    return soup_generator


class Requester:
    """Base class of requests maker like lawman and crawler 
       Provided With Simple request function and bs decorator 
    """

    def __init__(self, tieba_name="steam", cookie=None):
        if cookie is None:
            raise Exception("Cookie must be provided")

        self.session_worker = requests.Session()
        self.cookie = cookie
        self.tieba_base = TIEBA_MOBILE_BASE_URL.format(tieba_name=tieba_name)
        self.url_base = TIEBA_URL

    @bs4_decorator
    def get_content(self, url):
        """
        Get content of url with cookie
        :param url:
        :return String or None:
        """
        try:
            response = self.session_worker.get(url, cookies=self.cookie, timeout=10)

            logging.info('Get {0} succeed'.format(url))

            return response
        except requests.Timeout as e:
            logging.error('Get {0} failed : {1}'.format(url, e))
            return None
