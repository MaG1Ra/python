def file_line_generator(filename, max_length):
    with open(filename, 'r') as file:
        for line in file:
            trimmed_line = line[:max_length]
            reversed_words = ' '.join(map(lambda word: word[::-1], trimmed_line.split()))
            yield reversed_words

filename = 'example.txt'
max_length = 10

generator = file_line_generator(filename, max_length)
# mapped = map()

for line in generator:
    print(line)