from requester import Requester
from common import config_reader
import time
import spamword


class TiebaCrawler(Requester):
    """ Post crawler  , gather information of posts in given bar

        Get posts dict with { post_url : {'title':'post_title' , 'content':'postcontent'}} ,
        can't get image submmited in post
    """
    def __init__(self, tieba_name="steam", cookie=None):
        Requester.__init__(self, tieba_name, cookie)

    def __avaiable_check(self):
        # response = self.session_worker
        pass

    def get_posts_dict(self):
        soup = self.get_content(self.tieba_base)

        post_a = self.__get_posts_a(soup)
        titles_list = self.__get_posts_title(post_a)

        url_list = [self.url_base + tag.get('href') for tag in post_a]

        post_content_list = self.__get_posts_content(url_list)

        posts_dic = {url_list[index]: {'title': titles_list[index], 'content': post_content_list[index]} for index in
                     range(len(url_list))}

        return posts_dic

    def __get_posts_content(self, url_list):
        post_content_list_not_clean = [self.__get_post_content(url) for url in url_list]
        post_content_list = spamword.clean_spam_word(post_content_list_not_clean)
        return post_content_list

    def __get_posts_title(self, post_a):
        titles_list = [tag.text for tag in post_a]
        titles_list = [title[title.index('\xa0') + 1:].replace(u'\xa0', '') for title in titles_list]
        return titles_list

    def __get_posts_a(self, soup):
        posts_list = soup.findAll('div', {'class': 'i'})
        posts_list = [tag.find('a') for tag in posts_list if not tag.find('span', {'class': 'light'})]
        return posts_list

    def __get_post_content(self, post_url):
        content = self.get_content(post_url)

        post_content = content.find('div', {'class': 'i'}).text
        post_content = post_content.replace(u'\xa0', '')
        post_content = post_content[:post_content.index('回复')]
        post_content = post_content[4:]

        # time.sleep(1)

        return post_content


if __name__ == "__main__":
    cookie, _ = config_reader()
    tieba_worker = TiebaCrawler(cookie=cookie, tieba_name='steam')
    post_dic = tieba_worker.get_posts_dict()
    print(post_dic)
