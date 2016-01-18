import judger
import crawler
import lawman
import time
import random
from judgemethods import word_bags


def mainLoop(tieba_name='steam', cookie=None):
    tieba_crawlar = crawler.TiebaCrawler(tieba_name, cookie)
    tieba_judger = judger.Judger(word_bags)
    tieba_lawman = lawman.Lawman(tieba_name, cookie)

    print("Start crawling.....")
    post_dic = tieba_crawlar.get_posts_dict()
    for url in post_dic:
        if tieba_judger.judge(post_dic[url]):
            print("delete success")
            tieba_lawman.delete_post(url)

    print("Judge finished")

    time.sleep(random.randint(20, 30))


if __name__ == "__main__":
    cookie = {
        "BDUSS": "Wdpa35WQ2hTN2lIcjFOVkRrfll5MEpvaWV0Y3k0VjdSQ21abmZPb2ZuMXRucmhXQVFBQUFBJCQAAAAAAAAAAAEAAADRi6MwS0lESm91cm5leQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG0RkVZtEZFWa"}
    mainLoop('dota2提问', cookie)
