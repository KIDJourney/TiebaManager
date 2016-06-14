import judger
import crawler
import lawman
import time
import random
import logging
import importlib
from common import config_reader

try:
    import judgemethods
except Exception as e:
    logging.error("CAN'T LOAD JUDGE METHOD")
    raise e


class EventLoop:
    """
    Main process of the work.
    """

    def __init__(self, tieba_name='steam', cookie=None):
        self.tieba_name = tieba_name
        self.tieba_crawler = crawler.TiebaCrawler(tieba_name, cookie)
        self.tieba_judger = judger.Judger(judgemethods.POST_METHOD_LIST, judgemethods.REPLY_METHOD_LIST)
        self.tieba_lawman = lawman.Lawman(tieba_name, cookie)

    def loop(self):
        """
        Main Loop of the work :
        Work flow :
        Crawling Data (TiebaCrawler) -> Generate Post Objects (Post) -> Judge with info (Judger) -> Operator with post (Lawman)
        :return :
        """
        logging.info("LOOP BEGIN")
        self.reload_judge_method()

        logging.info('CRAWLING : {0}'.format(self.tieba_name))
        post_list = self.tieba_crawler.get_posts()
        logging.info("CRAWLING FINISH : {0}".format(self.tieba_name))

        logging.info('JUDGING {0} TASKS'.format(len(post_list)))

        post_delete_count, reply_delete_count, reply_count = self.judge(post_list)
        post_count = len(post_list)

        self.log_operator(post_count, post_delete_count, reply_count, reply_delete_count)

        logging.info("LOOP DONE")

        self.sleep()

    def log_operator(self, post_count, post_delete_count, reply_count, reply_delete_count):
        """
        Log the operator happened in this loop
        :param post_count:
        :param post_delete_count:
        :param reply_count:
        :param reply_delete_count:
        :return:
        """
        if self.tieba_judger.is_post_judge_empty():
            logging.info("POST JUDGE METHOD IS EMPTY")
        if self.tieba_judger.is_reply_judge_empty():
            logging.info("REPLAY JUDGE METHOD IS EMPTY")
        logging.info(
            "JUDGE DONE {0} POST judged {1} DELETE {2} REPLAYS JUDGE {3} DELETE".format(
                post_count, post_delete_count, reply_count, reply_delete_count))

    def reload_judge_method(self):
        """
        Reload the judge method
        """
        try:
            logging.info("RELOADING JUDGE METHOD")
            importlib.reload(judgemethods)
        except Exception as e:
            logging.error("RELOADING JUDGE METHOD FAILED : {0}".format(e))
        else:
            self.tieba_judger.update_judge_method(judgemethods.POST_METHOD_LIST, judgemethods.REPLY_METHOD_LIST)

    def judge(self, post_list):
        """
        Judge process of loop

        if post doesn't pass the judge :
            Delete by calling lawman
        else :
            if the reply in post doesn't pass the judge :
                Delete by calling lawman
        """
        post_delete_count = 0

        reply_delete_count = 0
        reply_count = 0

        for post in post_list:
            if self.tieba_judger.post_judge(post):
                if self.tieba_lawman.delete_post(post.get_del_url()):
                    logging.info("POST : {0} DELETE".format(post.get_title()))
                    post_delete_count += 1
                else:
                    logging.error("POST : {0} DELETE FAILED".format(post.get_title()))

            else:
                reply_count += len(post.reply_list)
                for reply in post.reply_list:
                    if self.tieba_judger.reply_judge(reply):
                        if self.tieba_lawman.delete_post(reply.get_del_url()):
                            logging.info("REPLY {0} DELETE".format(post.get_content()))
                            reply_delete_count += 1
                        else:
                            logging.error("REPLY {0} DELETE FAILED".format(reply.get_content()))

        return post_delete_count, reply_delete_count, reply_count

    def sleep(self):
        """
        Sleep random time after each loops.
        """
        time.sleep(random.randint(20, 30))


if __name__ == "__main__":
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')
    user_cookie, tieba_name = config_reader()
    loop = EventLoop('dota2提问', user_cookie)
    loop.loop()
