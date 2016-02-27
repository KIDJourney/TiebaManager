import requests
import json
import time
import logging

ENABLED_METHOD_LIST = []


def __enable_method(func):
    ENABLED_METHOD_LIST.append(func)
    return func


def judge_method_logger(func):
    def judege_logger(postobject):
        judge_result = func(postobject)

        logging.info(
                "Judging {0} {1} with {2}: {3}".format(postobject.get_title(), postobject.get_content(), func.__name__,
                                                       str(judge_result)))

        return judge_result

    return judege_logger


@judge_method_logger
def wordBags(post):
    with open('wordsbag.txt') as f:
        wordbag = f.read().split()

    content = post.get_title() + post.get_content()

    for word in wordbag:
        if word in content:
            return True
    return False


@judge_method_logger
def txNlpTextJudge(post):
    """
    Text emotion analyze provided by Tencent
    Page:http://nlp.qq.com/semantic.cgi#page4
    :param post:
    :return:
    """
    url = "http://nlp.qq.com/public/wenzhi/api/common_api.php"
    body = {'url_path': 'http://10.209.0.215:55000/text/sentiment',
            'body_data': ""}

    content = json.dumps({'content': post.get_title() + post.get_content()})
    body['body_data'] = content

    response = requests.post(url, data=body).json()

    time.sleep(1)

    return response['negative'] > 0.75

@__enable_method
@judge_method_logger
def patternCheck(post):
    """
    Check if title start with ['R', 'r', '【']
    :param post:
    :return boolean:
    """
    title = post.get_title()
    start_chr = ['R', 'r', '【']
    return title[0] not in start_chr


@judge_method_logger
def testJudge(post):
    """
    Judge method for debugging
    :param post:
    :return:
    """
    post_title = post.get_title()
    return post_title[0] == 'H'


if __name__ == "__main__":
    title = '求送'
