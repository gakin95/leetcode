def sortedSquaredArray(array):
    # Write your code here.
    sorted_squares = [0 for _ in array]
    start_ids = 0
    end_ids = len(array) - 1

    for i in reversed(range(len(array))):
        smaller_value = abs(array[start_ids])
        larger_value = abs(array[end_ids])
        if smaller_value > larger_value:
            sorted_squares[i] = smaller_value * smaller_value
            start_ids += 1
        else:
            sorted_squares[i] = larger_value * larger_value
            end_ids -= 1

    return sorted_squares
