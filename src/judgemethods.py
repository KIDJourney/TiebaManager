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

        if judge_result:
            desc = getattr(func, 'desc', '无说明')

            logging.info(
                "JUDGE {0} {1} : {2}".format(postobject.get_title(), postobject.get_content(), desc, ))

        return judge_result

    return judege_logger


def word_bags(post):
    word_bags.desc = "词袋"

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
    txNlpTextJudge.desc = "腾讯情感分析"

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
    pattern_check.desc = "标题格式"

    title = post.get_title()
    start_chr = ['R', 'r', '【', '[']
    return title[0] not in start_chr


@post_method
def test_judge(post):
    test_judge.desc = "测试函数"

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
