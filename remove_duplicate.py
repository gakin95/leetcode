from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1

        return insertIndex

class remove:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for reader in range(len(nums)):
            if nums[reader] != val:
                nums.append(nums[reader])
                count += 1

        nums[:count] = nums[-count:]
        nums = nums[:-count]
        print(count)
nums = [0,1,2,2,3,0,4,2]
print(nums[:4])
print(nums[-4:])
ans = remove()
print(ans.removeElement(nums,2))
