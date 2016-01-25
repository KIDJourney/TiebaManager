import bs4
import configparser


def bs4_decorator(function):
    def soup_generator(self, url):
        return bs4.BeautifulSoup(function(self, url).text)

    return soup_generator


def config_reader():
    config = configparser.ConfigParser()
    config.read('config.ini')

    cookie = config['setting']['cookie']
    tiebaName = config['setting']['tieba']

    cookie = {"BDUSS": cookie}

    return (cookie, tiebaName)


def config_intervaltime():
    config = configparser.ConfigParser()
    config.read('config.ini')

    return int(config['setting']['requestinterval'])


if __name__ == "__main__":
    print(config_reader())
