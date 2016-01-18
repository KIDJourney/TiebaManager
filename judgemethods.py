def word_bags(title, post):
    bags = ['求送', '点草', '草你', '傻逼', '权限狗', '操', '艹', '你妈', '灵车', \
            '老子', '孙子', '卡单', '不吹不黑', '平心而论', '就事论事']
    return sum([word in title or word in post for word in bags])


if __name__ == "__main__":
    title = '求送'
