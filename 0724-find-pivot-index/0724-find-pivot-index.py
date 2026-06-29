class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # concept 

        ## the left part of the index i in array is called prefix and the right part of the index is called as the suffix 

        # the array is represented like as below 

        #  0 , arr[i-x].....arr[i-1]  , arr[i] , arr[i+1], arr[i+2] .. arr[n-1]

        # so therefore the sum of the array is like  sum = prefix[i]+suffix[i]+arr[i]

        # here in this question lets say prefix[i] is termed as left and suffix is renamed as the right 

        left = 0 
        total = sum(nums)

        for i in range(len(nums)):
            right = total-left-nums[i]

            if  left == right : 
                return i 
            left += nums[i]
        return -1 

