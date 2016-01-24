class JudgeBase:
    """
    JudgeMethod base class , implement judge method
    All of subclass only accept two parameters
    """
    def judge(self, postTitle, postContent):
        pass


class WordsBag(JudgeBase):
    """
    Read word from file and detect if word is in post
    """
    def judge(self, postTitle, postContent):
        wordbag = []
        with open('wordsbag.txt') as f:
            wordbag = f.read().split()

        content = postTitle + postContent

        for word in wordbag:
            if word in content:
                return True
        return False


def word_bags(title, post):
    bags = []
    with open('wordsbag.txt') as f:
        bags = f.read().split()
    return sum([word in title or word in post for word in bags])


if __name__ == "__main__":
    title = '求送'
    judger = WordsBag()
    print(judger.judge(title, ''))
