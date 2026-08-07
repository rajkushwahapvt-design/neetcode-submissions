class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for num in nums:
            mp[num]=mp.get(num,0)+1
        ans=[]
        for _ in range(k):
            max_freq=-1
            max_num=-1
            for key in mp:
                if mp[key]>max_freq:
                    max_freq=mp[key]
                    max_num=key
            ans.append(max_num)
            del mp[max_num]
        return ans