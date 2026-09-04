class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        x = Counter(nums)
        return[ele for ele,freq in x.most_common(k)]
        