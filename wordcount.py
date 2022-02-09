import sys

"""Count words in file."""
def count_words(filename):
    text = open(filename)
    word_count = {}
    for line in text:
        words = line.split(" ")
        #print(type(words))
        #words = [word.strip(".,?") for word in words]
        for word in words:
            #print(type(word))
            word = word.strip(",.\n.?").lower()
            word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.items():
        print("{} {}".format(key, value))

file_name = sys.argv[1]
count_words(file_name)

