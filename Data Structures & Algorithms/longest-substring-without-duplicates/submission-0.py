class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_len = 0
    
        for right in range(len(s)):
            # s[R] が window にある間、L を進めて重複を消す
            while s[right] in window:
                window.remove(s[left])
                left += 1
            # s[R] を window に追加
            window.add(s[right])
            
            # 今の長さを記録
            max_len = max(max_len, right-left + 1)
        
        return max_len