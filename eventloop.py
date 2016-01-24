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
    tieba_judger = judger.Judger([judgemethods.WordsBag()])
    tieba_lawman = lawman.Lawman(tieba_name, cookie)

    logging.info('Starting crawling')
    post_dic = tieba_crawler.get_posts_dict()
    for url in post_dic:
        if tieba_judger.judge(post_dic[url]):
            tieba_lawman.delete_post(url)
            logging.info("{0} delete success".format(post_dic[url]['title']))

    logging.info("All judge finished")

    time.sleep(random.randint(20, 30))


if __name__ == "__main__":
    user_cookie, tieba_name = config_reader()
    mainloop(tieba_name, user_cookie)
