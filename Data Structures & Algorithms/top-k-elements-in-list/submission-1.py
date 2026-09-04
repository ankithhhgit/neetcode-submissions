class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 
        import heapq

        freq = Counter(nums)
        heap = []

        for key , val in freq.items():
            heapq.heappush(heap,(-val,key))

        res = []
        while len(res)<k:
            res.append(heapq.heappop(heap)[1])

        return res

        

        