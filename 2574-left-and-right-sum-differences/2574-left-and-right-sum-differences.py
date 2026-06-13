class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        total = sum(nums)
        A = [0]* len(nums)

        for i in range (len(nums)): 

            right = total-left-nums[i]

            #inserting in array 
            A[i]= abs(right - left) 

            left = left + nums[i]
        return A