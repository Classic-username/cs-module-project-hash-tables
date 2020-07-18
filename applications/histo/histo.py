# Your code here

with open('applications/histo/robin.txt') as f:
    words = f.read()

    ignore = (":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"", "?", "!")

    for char in ignore:
        words = words.replace(char, "")

    word_split = words.lower().split()


    cache = {}




    for word in word_split:
        if word not in cache:
            cache[word] = '#'
        else:
            cache[word] += '#'

    items = list(cache.items())

    items.sort(key=lambda x: x[1], reverse=True)

    for key, value in items:
        print(f'{key:<18} {value}')