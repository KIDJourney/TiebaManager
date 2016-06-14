import requests
import json
import time
import logging

# This module should be refacted soon

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
            "JUDGE {0} {1} WITH {2}: {3}".format(postobject.get_title(), postobject.get_content(), func.__name__,
                                                 str(judge_result)))

        return judge_result

    return judege_logger


def word_bags(post):
    with open('wordsbag.txt') as f:
        wordbag = f.read().split()

    content = post.get_title() + post.get_content()

    for word in wordbag:
        if word in content:
            return True
    return False


def txNlpTextJudge(post):
    """
        Text emotion analyze provided by Tencent
        Page:http://nlp.qq.com/semantic.cgi#page4
        :param post:
        :return:
        """
    url = "http://nlp.qq.com/public/wenzhi/api/common_api.php"
    body = {'api': 6,
            'body_data': ""}
    content = json.dumps({'content': post.get_title() + post.get_content()})
    body['body_data'] = content
    response = requests.post(url, data=body).json()
    time.sleep(1)
    return response['negative'] > 0.75


def pattern_check(post):
    """
        Check if title start with ['R', 'r', '【']
        :param post:
        :return boolean:
        """
    title = post.get_title()
    start_chr = ['R', 'r', '【', '[']
    return title[0] not in start_chr


@post_method
def test_judge(post):
    return '傻逼' in post.get_title()


POST_METHOD_LIST = [judge_method_logger(i) for i in POST_METHOD_LIST]
REPLY_METHOD_LIST = [judge_method_logger(i) for i in REPLY_METHOD_LIST]

if __name__ == "__main__":
    class foo():
        pass


    f = foo()

    f.get_title = lambda: "HHuck"
    f.get_content = lambda: 'HHHHH'
    f.get_author = lambda: 'KIDJourney'

    import copy

    j = copy.copy(f)
    j.get_author = lambda: 'HEHE'
