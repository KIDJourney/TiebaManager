from requester import Requester
from common import config_reader
from constant import *

class Lawman(Requester):
    """Posts and Users opeartor unit 

       Delete post with post url 
       Ban user with post url(Not avaiable now)  
    """

    def __init__(self, tieba_name="steam", cookie=None):
        Requester.__init__(self, tieba_name, cookie)

    def delete_post(self, delete_page_url):

        delete_page_response = self.get_content(delete_page_url)
        delete_confirm_url = delete_page_response.find('a', text='确认删除')
        delete_confirm_url = self.url_base + delete_confirm_url.get('href')

        delete_result = self.get_content(delete_confirm_url)

        return '成功删除' in delete_result.text

    def ban_user(self, post_url):
        # not avaiable in baidu now
        pass


if __name__ == "__main__":
    cookie, _ = config_reader()
    worker = Lawman(cookie=cookie)
    print(worker.delete_post())
