class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height = []  of length  n 
        # area of the container traed water inside = length * width 
        # therefore min(height[i],height[j]) * (j-i)

        i = 0
        j = len(height)-1

        max_area =  0

        while(i<j):

            current_area = min(height[i],height[j]) * (j-i)
            max_area = max(max_area, current_area)

            if height[i]<height[j]: # since lower value is bottleneck for area check for other valuesu 
                i = i+1
            else :
                j = j - 1

        return max_area