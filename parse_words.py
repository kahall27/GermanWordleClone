five_letter_set = set()

with open("words.txt", "r") as word_file:
    lines = word_file.readlines()
    for line in lines:
        if len(line.strip()) == 5:
            five_letter_set.add(line.strip().lower())

with open("five_letter_words.txt", "w") as write_file:
    for word in five_letter_set:
        write_file.write(word + "\n")
