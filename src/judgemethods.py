import requests
import json
import time
import logging

POST_METHOD_LIST = []
REPLY_METHOD_LIST = []


def reply_method(func):
    REPLY_METHOD_LIST.append(func)
    return func


def post_method(func):
    POST_METHOD_LIST.append(func)
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


@judge_method_logger
def replyTestJudge(reply):
    """
    Judge Method form Debugging
    :param reply:
    :return:
    """
    reply_content = reply.get_content()
    return reply_content[0] == 'H'


@reply_method
@judge_method_logger
def keyWordDected(reply):
    return "套现" in reply.get_content()


if __name__ == "__main__":
    title = '求送'
