def longestWord(a):
    string = ' '.join(a)
    new_words = string.split(' ')
    longest_word = new_words[0]
    for word in new_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word




print(longestWord(['hello chika', 'is kelvin']))