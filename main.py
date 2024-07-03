
def splitlist(numbers):
    idx = 0
    for x in range(len(numbers)):
        if numbers[x] < numbers[idx]:
            idx = x
    temp = numbers[0]
    numbers[0] = numbers[idx]
    numbers[idx] = temp
    first, *others = numbers
    return first, others


def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
