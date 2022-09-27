def partition(list):
    pivot = list[0]
    i = 1
    j = len(list) - 1
    while i <= j:
        if list[i] <= pivot:
            i += 1
        elif list[j] > pivot:
            j -= 1
        else:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1
    list[0], list[j] = list[j], list[0]


if __name__ == '__main__':
    list = [3, 7, 8, 4, 9, 10]
    partition(list)
    print(list)