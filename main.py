from eventloop import EventLoop
from common import config_reader
import logging

if __name__ == "__main__":
    cookie, tiebaName = config_reader()
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')
    eventLoop = EventLoop(tiebaName, cookie)
    while True:
        try:
            eventLoop.loop()
        except Exception as e:
            logging.warning(str(e))
