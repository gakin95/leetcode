def isValidSubsequence(array, sequence):
    # Write your code here.
    arr_ids = 0
    sub_index = 0
    while arr_ids < len(array) and sub_index < len(sequence):
        if array[arr_ids] == sequence[sub_index]:
            sub_index += 1
        arr_ids += 1
    return sub_index == len(sequence)