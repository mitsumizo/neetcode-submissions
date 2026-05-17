class Solution:
    def findMin(self, nums: List[int]) -> int:

        last_index = len(nums) - 1
        first_index = 0
        ans_min_number = nums[0]

        while first_index <= last_index:
            center_index = int((last_index + first_index) / 2)

            if nums[center_index] < ans_min_number:
                ans_min_number = nums[center_index]

            if nums[last_index] < nums[center_index]:
                first_index = center_index + 1
            else:
                last_index = center_index - 1

        return ans_min_number