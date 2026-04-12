class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low =  0 
        ans = float('inf')
        current_window = 0

        for high in range(len(nums)):
            current_window = current_window + nums[high]

            while(current_window>=target):
                #update the answer and shrink the window 
                length = high - low + 1
                ans = min (ans , length)

                #shrink window 
                current_window = current_window - nums[low]
                low = low + 1
                 
        return 0 if ans == float('inf') else ans  