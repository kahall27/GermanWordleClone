# Iterative binary search

def binary_search(my_list, target):
    lower_bound = 0
    upper_bound = len(my_list) - 1
    mid_point = 0

    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound) // 2

        if my_list[mid_point] > target:
            upper_bound = mid_point - 1
        elif my_list[mid_point] < target:
            lower_bound = mid_point + 1
        else:
            return True

    return False


if __name__ == "__main__":
    test_list = ["aa", "bb", "cc", "dd", "ee"]
    print(binary_search(test_list, "aa")) # should print True
    print(binary_search(test_list, "ff")) # should print False