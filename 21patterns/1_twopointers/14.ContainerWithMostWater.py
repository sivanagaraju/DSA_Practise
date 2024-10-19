def maxArea(heights):
        left, right = 0, len(heights)-1 
        print(right)
        max_area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
print(maxArea(heights=[1,8,6,2,5,4,8,3,7]))