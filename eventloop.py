import judger
import crawler
import lawman
import time
import random
import logging
import judgemethods
from common import config_reader


def mainloop(tieba_name='steam', cookie=None):

    tieba_crawler = crawler.TiebaCrawler(tieba_name, cookie)
    tieba_judger = judger.Judger([judgemethods.TxnlpTextJudge()])
    tieba_lawman = lawman.Lawman(tieba_name, cookie)

    logging.info('Starting crawling')
    post_list = tieba_crawler.get_posts()

    for post in post_list:
        if tieba_judger.judge(post):
            tieba_lawman.delete_post(post.get_del_url())
            logging.info("{0} delete success".format(post.get_title()))

    logging.info("All judge finished")

    time.sleep(random.randint(20, 30))


if __name__ == "__main__":
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')
    user_cookie, tieba_name = config_reader()
    mainloop('dota2提问', user_cookie)
