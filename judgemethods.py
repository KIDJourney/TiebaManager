import requests
import json
import time
import logging

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

    def judge(self, post):
        url = "http://nlp.qq.com/public/wenzhi/api/common_api.php"
        body = {'url_path': 'http://10.209.0.215:55000/text/sentiment',
                'body_data': ""}

        logging.info("Judging {0} {1}".format(post.get_title() , post.get_content()))

        content = json.dumps({'content': post.get_title() + post.get_content()})
        body['body_data'] = content

        response = requests.post(url, data=body).json()

        time.sleep(1)

        return response['negative'] > 0.75


if __name__ == "__main__":
    title = '求送'
    judger = WordsBag()
