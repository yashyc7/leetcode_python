class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0 
        windows_sum = 0 
        ans = float('inf')
        for high in range(len(nums)):
            windows_sum = windows_sum + nums[high]

            while(windows_sum>=target): 
                # update  answer :
                length= high-low+1 
                ans = min(ans,length)
                #shrink the window 
                windows_sum = windows_sum - nums[low] # remove low from infomrmation 
                low = low + 1

        return 0 if ans == float('inf') else ans  