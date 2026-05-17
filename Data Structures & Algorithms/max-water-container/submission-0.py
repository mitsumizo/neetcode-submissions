class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        p1 = 0 
        p2 = len(height) - 1
        max_h = max(height)
        Vmax = 0
        while p1 < p2:
            h1, h2 = height[p1], height[p2]
            Vcur = min(h1, h2) * (p2 - p1)  
            Vmax = max(Vmax, Vcur)

            if Vmax>(p2-p1)*max_h: # 2 ms optimization
                return Vmax

            if h1 < h2:
                p1+=1
            else:
                p2-=1
        return Vmax