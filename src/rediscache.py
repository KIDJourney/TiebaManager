import logging
import redis

from common import get_post_id


class postcache_dev:
    """
    Avoid many times connection to redis
    Untested
    """

    def __init__(self, func):
        self.func = func
        self.search_count = 0
        self.hit_count = 0

        try:
            self.redisclient = redis.StrictRedis()
        except Exception as e:
            logging.error("Redis server connect error")
            raise Exception("Redis error %s " % str(e))

    def __call__(self, url_list):
        print(self)
        url_not_cached = []
        for url in url_list:
            post_id = get_post_id(url)
            if self.redisclient.get(post_id):
                logging.info('Cache %s hit' % post_id)
                self.redisclient.expire(post_id, 600)
            else:
                logging.info('Caching %s' % post_id)
                self.redisclient.set(post_id, 'True')
                self.redisclient.expire(post_id, 600)
                url_not_cached.append(url)

        self.search_count = len(url_list)
        self.hit_count = len(url_list) - len(url_not_cached)

        return self.func(self, url_not_cached)


def postcache(func):
    """
    Decorator
    Cache the post url that have been crawled
    Check if the post have been crawled
    :param func:
    :return func:
    """

    def redischeck(instance, url_list):
        try:
            redisclient = redis.StrictRedis()
        except Exception as e:
            logging.error('Redis server connect error')
            raise e

        url_not_cached = []
        for url in url_list:
            post_id = get_post_id(url)
            if redisclient.get(post_id):
                logging.debug('Cache %s hit' % post_id)
                redisclient.expire(post_id, 600)
            else:
                logging.debug('Caching %s' % post_id)
                redisclient.set(post_id, 'True')
                redisclient.expire(post_id, 600)
                url_not_cached.append(url)

        query_count = len(url_list)
        cached = len(url_list) - len(url_not_cached)

        logging.info("{0} QUERY {1} CACHED HIT RATE {2}".format(query_count, cached, cached / len(url_list)))

        return func(instance, url_not_cached)

    return redischeck


if __name__ == "__main__":
    test_list = ['http://www.baidu.com/?kz={}'.format(i) for i in range(5000)]


    class Foo:
        @postcache_dev
        def print_list(self, urllist):
            print(self)
            print(len(urllist))


    f = Foo()
    f.print_list(test_list)
