from post import Post
import collections
import judgemethods


class Judger:
    """Post judge

       Classify a post into legal or illegal
       (Should Apply multiple judge method)
    """

    def __init__(self, methods=None):
        """
        Accept a list of judgemethod
        :param methods:
        :return:
        """
        if not isinstance(methods, collections.Iterable):
            raise Exception("The judge method must be iterable")
        if methods is None:
            raise Exception("The judge method can't be empty")

        self.methods = methods

    def judge(self, postobject):
        """
        Judge the post with all method the judge have.
        :param postobject:
        :return boolean:
        """
        for method in self.methods:
            if method.judge(postobject):
                return True
        return False

    def add_method(self, method):
        """
        Add method to the judger
        :param JudgeBase method:
        :return:
        """
        if not issubclass(method, judgemethods.JudgeBase):
            raise Exception("The method you add must implement JudgeBase")
        self.methods.append(method)
