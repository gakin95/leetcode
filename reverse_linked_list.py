# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed = []
        temp = head
        while temp:
            reversed.append(temp.val)
            temp = temp.next
        start = 0
        end = len(reversed) - 1
        while start < end:
            if reversed[start] != reversed[end]:
                return False
            start += 1
            end -= 1
        return True
