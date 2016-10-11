def words(word_string):
    word_list = word_string.split()
    count = {}
    for word in word_list:
        word = word.strip()
        if word.isdigit():
            word = int(word)
        if not word in count:
            count[word] = 1
        else:
          count[word] += 1
    return count