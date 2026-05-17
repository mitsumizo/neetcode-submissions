class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0

        for num in set_nums:
            if (num - 1) in set_nums:
                    continue
            count = 1
            while (num + count) in set_nums:
                count += 1
            if res < count:
                res = count
        return res
