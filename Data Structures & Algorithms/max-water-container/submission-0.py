class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        maxArea = -1
     
        left, right = 0, N-1

        while left < right: 
            width = right - left
            area = width * min(heights[left], heights[right])

            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
       

        return maxArea
