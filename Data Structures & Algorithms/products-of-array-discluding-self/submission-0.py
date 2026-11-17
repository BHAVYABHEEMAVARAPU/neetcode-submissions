import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        mul=math.prod(nums)
        z=nums.count(0)
        res=math.prod(x for x in nums if x!=0)
        for i in range(len(nums)):
            if z==0:
                ans=mul//nums[i]
                l.append(ans)
            elif z>1:
                l.append(0)
            else:
                if nums[i]==0:
                    l.insert(i,res)
                else:
                    l.append(0)
        return l










                


        