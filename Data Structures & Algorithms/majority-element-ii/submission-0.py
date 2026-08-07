class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1=0
        e2=0
        c1=0
        c2=0
        for num in nums:
            if num==e1:
                c1+=1
            elif num==e2:
                c2+=1
            elif c1==0:
                e1=num
                c1=1
            elif c2==0:
                e2=num
                c2=1
            else:
                c1-=1
                c2-=1
        c1=c2=0
        for num in nums:
            if e1==num:
                c1+=1
            if e2==num:
                c2+=1
        res=[]
        if c1>len(nums)//3:
            res.append(e1)
        if c2>len(nums)//3:
            res.append(e2)
        return res
            
      

        