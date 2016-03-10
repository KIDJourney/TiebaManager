from post import Post
import collections


class Judger:
    """Post judge
    Classify a post into legal or illegal
    """

    def __init__(self, post_method, reply_method):
        """Accept a list of judgemethod
        :param Iterable post_method:
        """
        if not isinstance(post_method, collections.Iterable):
            raise Exception("The post judge method must be iterable")
        if not isinstance(reply_method , collections.Iterable):
            raise Exception("The reply judge method must be iterable")

        self.post_methods = post_method
        self.reply_methods = reply_method

    def post_judge(self, postobject):
        """Judge the post with all post judge method the judger have.
        :param Post postobject:
        :return boolean:
        """
        for method in self.post_methods:
            if method(postobject):
                return True
        return False

    def reply_judge(self, reply_object):
        """Judge the reply with all reply judge method the judger have.
        :param reply_object:
        :return boolean:
        """
        for method in self.reply_methods :
            if method(reply_object) :
                return True
        return False

    def __judge(self, postobject):
        """
        Judge the post and post reply with all methods the judger have
        :param postobject:
        :return:
        """
        pass

    def add_method(self, method):
        """Add method to the instance
        :param callable method:
        :return:
        """
        if not callable(method):
            raise Exception("The method you add must implement JudgeBase")
        self.post_methods.append(method)
