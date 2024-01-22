def count_words(phrase):
    words = phrase.split()
    word_count_dict = {}

    for word in words:
        word_length = len(word)
        if word in word_count_dict:
            word_count_dict[word]["count"] += 1
        else:
            word_count_dict[word] = {"count": 1, "length": word_length}

    return word_count_dict
