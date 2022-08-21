write_file = open("five_letter_words.txt", "w")

with open("words.txt", "r") as word_file:
    prev_line = ""
    lines = word_file.readlines()
    for line in lines:
        if len(line.strip()) == 5 and (line.strip().lower() != prev_line):
            prev_line = line.strip().lower()
            write_file.write(prev_line + "\n")

write_file.close()
            

