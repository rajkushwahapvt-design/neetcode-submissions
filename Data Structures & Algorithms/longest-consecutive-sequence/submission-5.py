class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp=set(nums)
        ans=0
        count=0
        for num in mp:
            if num-1 not in mp:
                count=1
                curr=num
                while curr+1 in mp:
                    curr+=1
                    count+=1
                ans=max(ans,count)
        return ans