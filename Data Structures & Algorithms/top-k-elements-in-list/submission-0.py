class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        prevMap = {}
        for value in nums:
            prevMap[value] = prevMap.get(value, 0) + 1
        
        # 頻度(x[1])を基準に降順(reverse=True)でソート
        sorted_items = sorted(prevMap.items(), key=lambda x: x[1], reverse=True)
        
        # 上位k個のキー(要素)を取り出してリストで返す
        return [item[0] for item in sorted_items[:k]]