class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for string in s: 
            if string.isalnum():
                newString+= string.lower()
        return newString == newString[::-1]