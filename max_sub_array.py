from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur = 0
        max_sub = nums[1]
        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            max_sub = max(cur, max_sub)

        return max_sub

