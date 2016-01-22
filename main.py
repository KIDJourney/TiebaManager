from eventloop import mainLoop
from common import config_reader
import configparser

if __name__ == "__main__":
    cookie, tiebaName = config_reader()
    while True:
        mainLoop(tiebaName, cookie)
