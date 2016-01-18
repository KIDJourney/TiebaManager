class Judger:
    """Post judge

       Classify a post into legal or illegal
       (Should Apply multiple judge method)
    """

    def __init__(self, judge_method=None):
        if judge_method:
            self.judge_method = judge_method
        else:
            raise Exception("No judge method is provided")

    def judge(self, post_dict):
        post_title = post_dict['title']
        post_content = post_dict['content']

        return self.judge_method(post_title, post_content) > 0
