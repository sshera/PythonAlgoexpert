def isValidSubsequence(array, sequence):
    for number in sequence:
        prev_number = sequence[0]
        if number not in array:
            return False
        elif sequence.index(number) == 0:
            prev_number = number
        elif array.index(number) < array.index(prev_number):
            return False
        prev_number = number

    return True


array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, 10]

array2 = [23, 45, 67, 90, 84]
sequence2 = [23, 45, 67, 90, 85]

array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [-1, 1, 6, 10]

print(isValidSubsequence(array3, sequence3))
