final_file = open("five_letter_words.txt", "w")

with open("words.txt", "r") as word_file:
    lines = word_file.readlines()
    for line in lines:
        # line = line.strip()
        if len(line.strip()) == 5:
            final_file.write(line)

final_file.close()