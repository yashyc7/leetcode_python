class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low =0 
        total = 0 
        ans = float('inf')
        
        for high in range(len(nums)): 

            #include the information 

            total += nums[high]

            # while information is correct then shrink 
            while(total>=target): 
                length = high-low+1
                ans = min(ans,length)
                #now shrinking the window
                total = total - nums[low]
                low = low+1
        return 0 if ans == float('inf') else ans