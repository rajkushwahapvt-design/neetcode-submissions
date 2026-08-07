class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        ans=0
        mp={}
        for right in range(len(s)):
            if s[right] in mp and mp[s[right]]>=left:
                left=mp[s[right]]+1
            mp[s[right]]=right
            ans=max(ans,right-left+1)
        return ans
        