"""Count words in file."""
def count_words(filename):
    text = open(filename)
    word_count = {}
    for line in text:
        words = line.rstrip().split(" ")
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.items():
        print("{} {}".format(key, value))

count_words("test.txt")

