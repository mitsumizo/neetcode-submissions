class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []


        for index, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                last_index = stack.pop()
                res[last_index] = index - last_index
            # 今日の自分を「次は俺を救ってくれよな」とリストに入れる
            stack.append(index)
        return res 
