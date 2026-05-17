class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)

        for index in range(len(nums)):
            if index != 0 and sorted_nums[index] == sorted_nums[index-1]: 
                continue
            target = sorted_nums[index] * (-1)


            left_index = index + 1
            right_index = len(nums) - 1

            while left_index < right_index:
                cal_num = sorted_nums[left_index] + sorted_nums[right_index]

                if cal_num == target:
                    res.append([sorted_nums[index], sorted_nums[left_index], sorted_nums[right_index]])
                    left_index += 1
                    right_index -= 1
                    while left_index < right_index and sorted_nums[left_index] == sorted_nums[left_index - 1]:
                        left_index += 1
                        print("left: " + str(left_index))
                elif cal_num < target:
                    left_index += 1
                else :
                    right_index -= 1
        return res
