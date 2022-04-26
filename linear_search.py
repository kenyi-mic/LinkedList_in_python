def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("The target is at index: ", index)

    else:
        print("The target is not found!")


numbers = [1, 12, 4, 5, 21, 7, 8, 9]

result = linear_search(numbers, 12)

verify(result)
