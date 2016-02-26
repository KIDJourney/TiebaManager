import requests
import json
import time
import logging


def judge_method_logger(func):
    def judege_logger(instance, postobject):
        judge_result = func(instance, postobject)

        logging.info(
                "Judging {0} {1} : {2}".format(postobject.get_title(), postobject.get_content(), str(judge_result)))

        return judge_result

    return judege_logger


class JudgeBase:
    """
    JudgeMethod base class , implement judge method
    All of subclass only accept two parameters
    """

    def judge(self, post):
        pass


class WordsBag(JudgeBase):
    """
    Read word from file and detect if word is in post
    """

    @judge_method_logger
    def judge(self, post):
        wordbag = []
        with open('wordsbag.txt') as f:
            wordbag = f.read().split()

        content = post.get_title() + post.get_content()

        for word in wordbag:
            if word in content:
                return True
        return False


class TxnlpTextJudge(JudgeBase):
    """
    Text emotion analyze provided by Tencent
    Page:http://nlp.qq.com/semantic.cgi#page4
    """

    @judge_method_logger
    def judge(self, post):
        url = "http://nlp.qq.com/public/wenzhi/api/common_api.php"
        body = {'url_path': 'http://10.209.0.215:55000/text/sentiment',
                'body_data': ""}

        content = json.dumps({'content': post.get_title() + post.get_content()})
        body['body_data'] = content

        response = requests.post(url, data=body).json()

        time.sleep(1)

        return response['negative'] > 0.75


class TestJudge(JudgeBase):
    """
    Judge for debugging
    """

    def judge(self, post):
        post_title = post.get_title()
        return post_title[0] == 'H'


if __name__ == "__main__":
    title = '求送'
