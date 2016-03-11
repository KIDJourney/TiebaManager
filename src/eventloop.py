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
    """

    def __init__(self, tieba_name='steam', cookie=None):
        self.tieba_name = tieba_name
        self.tieba_crawler = crawler.TiebaCrawler(tieba_name, cookie)
        self.tieba_judger = judger.Judger(judgemethods.POST_METHOD_LIST, judgemethods.REPLY_METHOD_LIST)
        self.tieba_lawman = lawman.Lawman(tieba_name, cookie)

    def loop(self):
        """Main Loop of the work :
        Work flow :
        Crawling Data (TiebaCrawler) -> Generate Post Objects (Post) -> Judge with info (Judger) -> Operator with post (Lawman)
        :return :
        """
        logging.info('Crawling start : {0}'.format(self.tieba_name))
        post_list = self.tieba_crawler.get_posts()
        logging.info("Crawling finish : {0}".format(self.tieba_name))

        logging.info('Judging Start , {0} tasks in queue'.format(len(post_list)))

        post_delete_count, reply_delete_count, reply_count = self.judge(post_list)

        logging.info(
            "Judging finish , {0} post(s) judged , {1} post(s) delete , {2} reply(s) judged , {3} reply(s) delete.".format(
                len(post_list), post_delete_count, reply_count, reply_delete_count))

        logging.info("Loop finish")

        self.sleep()

    def judge(self, post_list):
        post_delete_count = 0

        reply_delete_count = 0
        reply_count = 0

        for post in post_list:
            if self.tieba_judger.post_judge(post):
                if self.tieba_lawman.delete_post(post.get_del_url()):
                    logging.info("Post : {0} delete success".format(post.get_title()))
                    post_delete_count += 1
                else:
                    logging.error("Post : {0} delete Failed !".format(post.get_title()))

            else:
                reply_count += len(post.reply_list)
                for reply in post.reply_list:
                    if self.tieba_judger.reply_judge(reply):
                        if self.tieba_lawman.delete_post(reply.get_del_url()):
                            logging.info("Reply {0} delete success".format(post.get_content()))
                            reply_delete_count += 1
                        else:
                            logging.error("{0} delete Failed !".format(reply.get_content()))

        return post_delete_count, reply_delete_count, reply_count

    def sleep(self):
        time.sleep(random.randint(20, 30))


if __name__ == "__main__":
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')
    user_cookie, tieba_name = config_reader()
    loop = EventLoop('dota2提问', user_cookie)
    loop.loop()
