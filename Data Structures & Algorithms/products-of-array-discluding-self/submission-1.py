class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_val_list = [1]
        right_val_list = [1]

        for num in nums[:-1]:
            left_val_list.append(left_val_list[-1] * num)

        for num in reversed(nums[1:]):
            right_val_list.append(right_val_list[-1] * num)

        right_val_list = list(reversed(right_val_list))

        return [
            left_val_list[index] * right_val_list[index] for index in range(len(nums))
        ]
