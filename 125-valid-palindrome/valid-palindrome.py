class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for char in s:
            if char.isalnum():
                a += char.lower()
        
        for i in range(len(a)):
            if a[i] != a[-(i+1)]:
                return False
        return True
        