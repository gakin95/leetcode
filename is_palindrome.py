# def isPalindrome(string):
#     # Write your code here.
#     reversed_string = []
#     for char in string:
#         reversed_string.append(char)
#     print("".join(reversed_string))
#     return "".join(reversed_string) == string

def isPalindrome(string):
    # Write your code here.
    start = 0
    end = len(string) - 1
    while start < int(len(string) / 2):
        print(start)
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


string = "abcdabc"
print(isPalindrome(string))

# print(int(len(string)/2))
