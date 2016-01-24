import collections
import judgemethods


class Judger:
    """Post judge

       Classify a post into legal or illegal
       (Should Apply multiple judge method)
    """

    def __init__(self, methods=None):
        if not isinstance(methods, collections.Iterable):
            raise Exception("The judge method must be iterable")
        if methods is None:
            raise Exception("The judge method can't be empty")

        self.methods = methods

    def judge(self, postdict):
        post_title = postdict['title']
        post_content = postdict['content']

        for method in self.methods:
            if method.judge(post_title, post_content):
                return True

        return False

    def add_method(self, method):
        if not issubclass(method, judgemethods.JudgeBase):
            raise Exception("The method you add must implement JudgeBase")
        self.methods.append(method)
