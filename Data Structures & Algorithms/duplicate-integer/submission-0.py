class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = dict()

        for num in nums:
            if num in prevMap:
                return True
            prevMap[num] = 1
        return False
