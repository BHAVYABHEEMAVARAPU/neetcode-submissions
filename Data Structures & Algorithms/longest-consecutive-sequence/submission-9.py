class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long=0
        l=set(nums)
        for num in l:
            if num-1 not in l:
                curr_num=num
                c=1
                while (curr_num+1) in l:
                    curr_num=curr_num+1
                    c=c+1
                long=max(long,c)    
        return long