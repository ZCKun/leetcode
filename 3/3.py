class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _map = dict()
        j = 0
        ans = 0
        for i, c in enumerate(list(s)):
            if c in _map:
                j = max(_map.get(c), j)
            ans = max(ans, i - j + 1)
            _map.update({c: i+1})
        return ans
    

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))