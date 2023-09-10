def subarray_sum(nums, target):
    sum_dict = {0: -1}
    cum_sum = 0
    for i, num in enumerate(nums):
        cum_sum += num
        diff = cum_sum - target
        if diff in sum_dict:
            return [sum_dict[diff] + 1, i]
        sum_dict[cum_sum] = i

    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
