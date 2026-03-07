class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k]) 
        max_sum = window_sum 

        for i in range(k,len(nums)):

            # remove old element and add next element
            window_sum = window_sum - nums[i-k] # rmove first element of the first window since we are going to shift windows 
            window_sum = window_sum + nums[i] # increase window to check 

            max_sum = max(max_sum , window_sum)

        return max_sum/float(k)
        