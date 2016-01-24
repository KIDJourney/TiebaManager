from eventloop import mainloop
from common import config_reader
import logging

if __name__ == "__main__":
    cookie, tiebaName = config_reader()
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')
    while True:
        try:
            mainloop(tiebaName, cookie)
        except Exception as e:
            logging.warn(str(e))
