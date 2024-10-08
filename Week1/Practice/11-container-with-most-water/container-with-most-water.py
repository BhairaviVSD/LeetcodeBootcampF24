class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_index, end_index = 0, len(height)-1
        max_area = 0
        while start_index <= end_index:
            if ((min(height[start_index], height[end_index]))*(end_index-start_index) > max_area):
                max_area = (min(height[start_index], height[end_index]))*(end_index-start_index)
            if (height[start_index] > height[end_index]): end_index -= 1
            elif (height[start_index] < height[end_index]): start_index +=1
            else: 
                start_index +=1
                end_index -= 1
        return max_area
