from requester import Requester
from common import config_reader, config_intervaltime
import post
import time
import rediscache
import logging


class TiebaCrawler(Requester):
    """
    Post crawler  , gather information of posts in given bar
    can't get image submitted in post
    """

    def __init__(self, tieba_name="steam", cookie=None):
        """
        Initialize Crawler
        :param tieba_name:
        :param cookie:
        """
        Requester.__init__(self, tieba_name, cookie)

        self.__available_check()

    def __available_check(self):
        """
        Checking cookie available , tieba existence , manage rights validity
        :return boolean:
        """
        logging.info("Cookie Available Check")

        response = self.get_content(self.tieba_base)

        if "参与本吧讨论请先" in response:
            logging.error("Cookie Available Check : FAILED")
            raise Exception("User Cookie not available")

        logging.info("Checked")

        logging.info("Checking Tieba Existence......")
        if "尚未建立" in response:
            logging.error("Checking Tieba Existence : FAILED")
            raise Exception("{0} doesn't exist".format(self.tieba_name))

        logging.info("Checked")

        logging.info("All check done")
        return True

    def get_posts(self):
        """
        Get all posts on first page of tieba , and generate a post objects list
        :return list of Post object:
        """
        soup = self.get_content(self.tieba_base)

        post_attr = self.__get_posts_url_postfix(soup)

        url_list = [self.url_base + tag for tag in post_attr]

        post_dict = self.__get_content_list(url_list)
        post_list = [post.Post(url, soup) for url, soup in post_dict.items()]

        return post_list

    def __get_posts_url_postfix(self, soup):
        """
        Get all post url postfix from the soup of first page of first page
        :param soup:
        :return list of posts' postfix url:
        """
        posts_list = soup.findAll('div', {'class': 'i'})
        # find divs of all posts
        posts_list = [tag.find('a').get('href') for tag in posts_list if not tag.find('span', {'class': 'light'})]
        # get all url postfixes of posts except excellent post
        return posts_list

    @rediscache.postcache
    def __get_content_list(self, url_list):
        """
        Get post content with given url list
        :param url_list:
        :return dict:
        """
        content_list = {}

        for url in url_list:
            content = self.get_content(url)
            if content:
                content_list[url] = content

            time.sleep(config_intervaltime())

        return content_list


if __name__ == "__main__":
    cookie, _ = config_reader()
    tieba_worker = TiebaCrawler(cookie=cookie, tieba_name='dota2提问')
    posts = tieba_worker.get_posts()
    # print((list(map(str, posts))))
    # posts = tieba_worker.get_posts()
    # print((list(map(str, posts))))
    # print(list(map(str, posts[0].reply_list)))
