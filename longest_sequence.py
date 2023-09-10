def longestConsecutive(nums):
    nums_set = set(nums)
    longest_sequence = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            cur_num = num
            count = 1
            while cur_num + 1 in nums_set:
                cur_num += 1
                count += 1
            longest_sequence = max(longest_sequence, count)
    return longest_sequence


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
