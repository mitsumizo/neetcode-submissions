class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0

        for num in set_nums:
            if (num - 1) in set_nums:
                    continue
            found = True
            count = 1
            while found:
                target_num = num + count
                if target_num in set_nums:
                    count += 1
                    continue
                if res < count:
                    res = count
                found = False
                
        return res
