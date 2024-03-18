class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,length = 0,0,0
        hm = {}
        while r < len(s):
            if s[r] in hm:
                l = max(l,hm[s[r]]+1)
            hm[s[r]] = r
            length = max(length,r-l+1)
            r += 1
        return length
        