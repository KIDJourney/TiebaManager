from eventloop import EventLoop
from common import config_reader
import logging
import sys, os

if __name__ == "__main__":
    cookie, tiebaName = config_reader()
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')
    eventLoop = EventLoop(tiebaName, cookie)
    while True:
        try:
            eventLoop.loop()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            logging.warning("Error :{0} of {1}  on {2}:{3} ".format(str(e), exc_type, fname, exc_tb.tb_lineno))
