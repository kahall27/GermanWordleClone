# account for characters with umlauts (ä, ö, ü)
def remove_umlauts(word):
    if "ä" in word:
        word = word.replace("ä", "a")
    if "ö" in word:
        word = word.replace("ö", "o")
    if "ü" in word:
        word = word.replace("ü", "u")
    return word

# Iterative binary search
def binary_search(my_list, target):
    target = remove_umlauts(target)
    lower_bound = 0
    upper_bound = len(my_list) - 1
    mid_point = 0

    while lower_bound <= upper_bound:
        mid_point = lower_bound + ((upper_bound - lower_bound) // 2)
        word_to_check = my_list[mid_point]

        # account for characters with umlauts
        word_to_check = remove_umlauts(word_to_check)

        if word_to_check > target:
            upper_bound = mid_point - 1
        elif word_to_check < target:
            lower_bound = mid_point + 1
        else:
            return True

    return False


if __name__ == "__main__":
    test_list = ["aa", "ää", "bb", "cc", "dd", "ee"]
    print(binary_search(test_list, "ää")) # should print True
    print(binary_search(test_list, "ff")) # should print False