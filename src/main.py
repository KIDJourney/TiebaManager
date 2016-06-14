from eventloop import EventLoop
from common import config_reader
import logging
import sys, os

if __name__ == "__main__":
    cookie, tiebaName = config_reader()

    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.getLogger('requests').setLevel(logging.WARNING)

    eventLoop = EventLoop(tiebaName, cookie)

    while True:
        try:
            eventLoop.loop()
        except Exception as e:
            logging.error("Service crashed : {0}".format(e))
