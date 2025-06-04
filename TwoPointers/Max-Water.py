from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        solution = 0
        while left < right:
            area = (right - left) * (min(heights[right], heights[left]))
            if area > solution:
                solution = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return solution
               

solution = Solution()
print(solution.maxArea([1,7,2,5,4,7,3,6]))