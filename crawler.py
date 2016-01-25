from requester import Requester
from common import config_reader
import post
import time
import spamword


class TiebaCrawler(Requester):
    """ Post crawler  , gather information of posts in given bar
        can't get image submmited in post
    """
    def __init__(self, tieba_name="steam", cookie=None):
        Requester.__init__(self, tieba_name, cookie)

    def __avaiable_check(self):
        # response = self.session_worker
        pass

    def get_posts(self):
        soup = self.get_content(self.tieba_base)

        post_a = self.__get_posts_a(soup)

        url_list = [self.url_base + tag.get('href') for tag in post_a]

        post_content_list = [self.get_content(url) for url in url_list]
        post_list = [post.Post(url, soup) for url, soup in zip(url_list, post_content_list)]

        return post_list

    def __get_posts_a(self, soup):
        posts_list = soup.findAll('div', {'class': 'i'})
        posts_list = [tag.find('a') for tag in posts_list if not tag.find('span', {'class': 'light'})]
        return posts_list


if __name__ == "__main__":
    cookie, _ = config_reader()
    tieba_worker = TiebaCrawler(cookie=cookie, tieba_name='dota2提问')
    posts = tieba_worker.get_posts()
    print(list(map(str, posts)))
    print(list(map(str, posts[0].reply_list)))
