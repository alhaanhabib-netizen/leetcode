class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        for i in range(len(nums)):
            if nums[i]==target:
                a=i
                break
            else:
                a=-1
        return a
        