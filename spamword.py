SPAM_WORDS = ['图']


def clean_spam_word(content_list):
    post_content_list = [''.join(i for i in content if i not in SPAM_WORDS) for content in content_list]

    return post_content_list
