class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        return sorted(a) == sorted(b)   
        