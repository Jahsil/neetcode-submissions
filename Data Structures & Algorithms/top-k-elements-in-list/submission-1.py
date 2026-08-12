class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        numsCount = {}
        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1

        heap = []
        for ky, v in numsCount.items():
            heapq.heappush(heap, (-v, ky))
        for count in range(k):
            ans.append((heapq.heappop(heap)[1]))
        return ans