import judger
import crawler
import lawman
import time
import random
import logging
import judgemethods
from common import config_reader


class EventLoop:
    """Main process of the work.
    Crawling Data (TiebaCrawler) -> Generate Post Objects (Post) -> Judge with info (Judger) -> Operator with post (Lawman)
    """
    def __init__(self, tieba_name='steam', cookie=None):
        self.tieba_name = tieba_name
        self.tieba_crawler = crawler.TiebaCrawler(tieba_name, cookie)
        self.tieba_judger = judger.Judger(judgemethods.ENABLED_METHOD_LIST)
        self.tieba_lawman = lawman.Lawman(tieba_name, cookie)

    def loop(self):
        logging.info('Crawling start : {0}'.format(self.tieba_name))
        post_list = self.tieba_crawler.get_posts()
        logging.info("Crawling finish : {0}".format(self.tieba_name))

        logging.info('Judging Start , {0} tasks in queue'.format(len(post_list)))
        delete_count = 0
        for post in post_list:
            if self.tieba_judger.judge(post):
                self.tieba_lawman.delete_post(post.get_del_url())
                logging.info("{0} delete success".format(post.get_title()))
                delete_count += 1
        logging.info("Judging finish , {0} tasks judged , {1} tasks delete".format(len(post_list), delete_count))

        logging.info("Loop finish")

        self.sleep()

    def sleep(self):
        time.sleep(random.randint(20, 30))

if __name__ == "__main__":
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')
    user_cookie, tieba_name = config_reader()
    loop = EventLoop('dota2提问', user_cookie)
    loop.loop()
