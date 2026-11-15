class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=set()
        n=len(nums)

        for i in range(0,n):
            for j in range(n-1,0,-1):
                
                if i!=j and nums[i]+ nums[j]==target:
                    l.add(i)
                    l.add(j)
                    break
        return list(l)
            