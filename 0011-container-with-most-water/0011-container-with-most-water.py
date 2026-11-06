class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            if area > best:
                best = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best