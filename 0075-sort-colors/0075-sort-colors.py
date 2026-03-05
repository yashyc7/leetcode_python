class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0 #start pointer to an array  
        end = n -1 # end pointer to an array 
        mid = 0 # pointer for decision making 

        #if we get the 0 at the middle then swap with start pointer because the 0's should be at start
        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
        return nums

        