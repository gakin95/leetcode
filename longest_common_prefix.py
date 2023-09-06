from typing import List


# def longestCommonPrefix(strs: List[str]) -> str:
#     if not strs:
#         return ""
#     min_string = min(strs, key=len)
#     for i, char in enumerate(min_string):
#         for str in strs:
#             if str[i] != char:
#                 return min_string[:i]
#     return min_string

def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Find the string with the smallest length
    minStr = min(strs, key=len)

    # Setting the range for binary search
    low, high = 0, len(minStr)

    while low <= high:
        mid = (low + high) // 2
        if isCommonPrefix(strs, mid):
            low = mid + 1
        else:
            high = mid - 1

    # Return the common prefix of length (low - 1)
    return minStr[:low - 1]


def isCommonPrefix(strs, length):
    prefix = strs[0][:length]
    for i in range(1, len(strs)):
        if not strs[i].startswith(prefix):
            return False
    return True


# Test
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))  # Outputs: "fl"


