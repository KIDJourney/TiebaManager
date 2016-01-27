import redis

def postcache(func):
    def redischeck(instance, url_list):
        redisclient = redis.StrictRedis()
        url_not_cached = []
        for url in url_list:
            if redisclient.get(url):
                redisclient.expire(url, 600)
            else:
                redisclient.set(url, 'True')
                redisclient.expire(url, 600)
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
