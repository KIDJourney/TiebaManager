import gevent.monkey
gevent.monkey.patch_all()
import requests


class CalwerBase:
    def __init__(self, sesion=None, cookie=None):
        pass
