class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for reader in range(len(nums)):
            if nums[reader] != val:
                nums.append(nums[reader])
                count += 1

        nums[:count] = nums[-count:]
        nums = nums[:-count]
        return count

        # writer = 0
        # for reader in range(len(nums)):
        #     if nums[reader] != val:
        #         nums[writer] = nums[reader]
        #         writer += 1
        # return writer
        # reader = 0
        # while reader < len(nums):
        #     if nums[reader] == val:
        #         reader += 1
        #     else:
        #         nums[writer] = nums[reader]
        #         reader += 1
        #         writer += 1
        # return writer





