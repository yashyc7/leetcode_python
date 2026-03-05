class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low = 0  # starting the lowest pointer at first element of the array
        high = 0  # starting the high pointer also at the first element of the array 
        result = float('inf')  # we want minimum length, so start with +infinity
        n = len(nums)
        sum = 0  # suppose default sum is zero 

        while (high < n):  # high must not pass length of the array 
            sum = sum + nums[high]  # first window sum 

            while (sum >= target):  # while sum is greaterthan equal to target then eliminate them untill we get smallest subarray size
                length = high - low + 1  # for eg size of array 0,2 is litteraly 2-0+1 =3 as 0,1,2
                result = min(length, result)  # take minimum length

                # now update the sum after result calculated we must proceed to elimintate things untill we get optimal size
                sum = sum - nums[low]

                # now remove / fire the old ones since we can still acheive to target
                low = low + 1  # shrink the window
            
            # outside of the inner while loop increase the size of the windows 
            high = high + 1 

        return 0 if result == float('inf') else result