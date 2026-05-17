class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer_list = [1 for i in range(len(nums))]

        # Leftを作成する
        left = [1 for i in range(len(nums))]
        for index in range(1,len(nums)):
            left[index] = left[index - 1] * nums[index - 1]

        # Rightを作成する
        right = [1 for i in range(len(nums))]
        for index in range(len(nums) - 2, -1, -1):
            right[index] = right[index + 1] * nums[index + 1]

        for index in range(0,len(nums)):
            answer_list[index] = left[index] * right[index]
            
        return answer_list
