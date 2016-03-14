from requester import Requester
from common import config_reader
from common import get_post_id
from constant import *
from bs4 import BeautifulSoup
import json
import re

class Lawman(Requester):
    """Posts and Users operator unit
       Delete post with post url
       Ban user with post url(Not available now)
    """

    def __init__(self, tieba_name="steam", cookie=None):
        Requester.__init__(self, tieba_name, cookie)
        self.ban_url = TIEBA_BAN_URL

    def delete_post(self, delete_page_url):
        """Delete given url
        :param delete_page_url:
        :return boolean:
        """
        delete_page_response = self.get_content(delete_page_url)
        delete_confirm_url = delete_page_response.find('a', text='确认删除')
        delete_confirm_url = self.url_base + delete_confirm_url.get('href')

        delete_result = self.get_content(delete_confirm_url)

        return '成功删除' in delete_result.text

    def ban_user(self, post_url, author,reason):
        # not avaiable in baidu now
        tbs_re = re.compile(r'"tbs": "(\S+)"')
        fid_re = re.compile(r"fid:'(\d+)'")

        post_id = get_post_id(post_url)[0]
        post_url = "http://tieba.baidu.com/p/{0}".format(post_id)
        response = self.get_content(post_url)

        tbs = tbs_re.search(response.text).group(1)
        fid = fid_re.search(response.text).group(1)

        data_field =  response.find('div' , {'class':'l_post l_post_bright j_l_post clearfix  '}).get('data-field')
        json_object = json.loads(data_field)
        pid = json_object['content']['post_id']

        form_data = {'day':1 , 'fid':fid , 'tbs':tbs , 'ie':'gbk' , 'user_name[]':"寒饼干" , 'pid[]':pid , 'reason':'Test'}

        response = self.session_worker.post(self.ban_url ,cookies = self.cookie , data=form_data)

if __name__ == "__main__":
    cookie, _ = config_reader()
    worker = Lawman(cookie=cookie)
    print(worker.ban_user("http://tieba.baidu.com/mo/q---189C1660F1F72884A696954D1ED81373%3AFG%3D1--1-3-0--2--wapp_1457786153016_691/m?kz=4408346413&is_bakan=0&lp=5010&pinf=1_2_0" ,'寒饼干' , "Test"))
