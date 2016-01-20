def word_bags(title, post):
    bags = []
    with open('wordbags.txt') as f :
        bags = f.read().split()
    return sum([word in title or word in post for word in bags])

if __name__ == "__main__":
    title = '求送'