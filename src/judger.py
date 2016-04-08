from post import Post
import collections


class Judger:
    """
    Post judge
    Classify a post into legal or illegal
    """

    def __init__(self, post_method, reply_method):
        """
        Accept a list of judgemethod
        :param Iterable post_method:
        """
        if not isinstance(post_method, collections.Iterable):
            raise Exception("The post judge method must be iterable(list or tuple)")
        if not isinstance(reply_method, collections.Iterable):
            raise Exception("The reply judge method must be iterable(list or tuple)")

        self.post_methods = post_method
        self.reply_methods = reply_method

    def post_judge(self, postobject):
        """
        Judge the post with all post judge method the judger have.
        :param Post postobject:
        :return boolean:
        """
        for method in self.post_methods:
            if method(postobject):
                return True
        return False

    def reply_judge(self, reply_object):
        """
        Judge the reply with all reply judge method the judger have.
        :param reply_object:
        :return boolean:
        """
        for method in self.reply_methods:
            if method(reply_object):
                return True
        return False

    def update_judge_method(self, post_method, replay_method):
        """
        Reset judge methods
        :param post_method:
        :param replay_method:
        :return:
        """
        self.post_methods = post_method
        self.reply_methods = replay_method

    def is_post_judge_empty(self):
        return len(self.post_methods) == 0

    def is_reply_judge_empty(self):
        return len(self.reply_methods) == 0

