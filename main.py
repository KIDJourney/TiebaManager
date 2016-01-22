from eventloop import mainLoop
from common import config_reader
import configparser
import logging

if __name__ == "__main__":
    cookie, tiebaName = config_reader()
    logging.basicConfig(filename='log.txt',level = logging.DEBUG , format='%(asctime)s %(message)s')
    while True:
        mainLoop(tiebaName, cookie)
