import configparser
from urllib import parse


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


def get_post_id(url):
    """
    Get post id from url
    :param url:
    :return string:
    """
    try:
        url = parse.urlparse(url)
        query = url.query
        post_id = parse.parse_qs(query)['kz']
    except KeyError:
        post_id = ["HomePage"]

    return post_id[0]


if __name__ == "__main__":
    print(config_reader())
