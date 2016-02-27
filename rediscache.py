import logging
import redis

from common import get_post_id


def postcache(func):
    """Decorator
    Cache the post url that have been crawled
    Check if the post have been crawled
    :param func:
    :return func:
    """

    def redischeck(instance, url_list):
        redisclient = redis.StrictRedis()
        url_not_cached = []
        for url in url_list:
            post_id = get_post_id(url)
            if redisclient.get(post_id):
                logging.info('Cache %s hit' % post_id)
                redisclient.expire(post_id, 600)
            else:
                logging.info('Caching %s' % post_id)
                redisclient.set(post_id, 'True')
                redisclient.expire(post_id, 600)
                url_not_cached.append(url)
        return func(instance, url_not_cached)

    return redischeck

# class PostCache:
#     def __init__(self, func):
#         self.func = func
#         self.redis = redis.StrictRedis()
#
#     def __call__(self, url_list):
#         url_not_cached = []
#         for url in url_list:
#             if self.redis.get(url):
#                 self.redis.expire(url, 600)
#             else:
#                 url_not_cached.append(url)
#                 self.redis.set(url, '1')
#                 self.redis.expire(url, 600)
#
#         return self.func(url_not_cached)
