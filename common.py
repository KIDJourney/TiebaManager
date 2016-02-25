import bs4
import configparser


def bs4_decorator(function):
    """
    Decorator
    Generator a soup from give html content
    :param function:
    :return:
    """
    def soup_generator(self, url):
        return bs4.BeautifulSoup(function(self, url).text)

    return soup_generator


def config_reader():
    """
    Read tieba name and cookie from config file
    :return Tuple (cookie , tiebaName):
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    cookie = config['setting']['cookie']
    tiebaName = config['setting']['tieba']

    cookie = {"BDUSS": cookie}

    return (cookie, tiebaName)


def config_intervaltime():
    """
    Read intervaltime from config file
    :return integer:
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    return int(config['setting']['requestinterval'])


if __name__ == "__main__":
    print(config_reader())
