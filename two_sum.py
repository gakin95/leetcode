# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> tuple[int, int]:
        dic = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dic:
                return i, dic[diff]
            dic[num] = i


my_sum = Solution()
print(my_sum.twoSum([2, 7, 11, 15], 9))
