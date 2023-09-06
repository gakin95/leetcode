from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    min_string = min(strs, key=len)
    for i, char in enumerate(min_string):
        for str in strs:
            if str[i] != char:
                return min_string[:i]
    return min_string


strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))