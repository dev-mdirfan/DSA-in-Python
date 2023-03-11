def LinearSearch(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return index
    return -1

if __name__ == "__main__":
    