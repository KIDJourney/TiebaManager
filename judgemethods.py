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

if __name__ == "__main__":
    title = '求送'
    judger = WordsBag()
