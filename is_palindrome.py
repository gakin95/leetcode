def isPalindrome(string):
    # Write your code here.
    reversed_string = ""
    for char in reversed(string):
        reversed_string += char
    print(string == reversed_string)

isPalindrome("abc")

