class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in sorted(freq,key=freq.get,reverse=True):
            l.append(num)
        return l[:k]