class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low =  0
        ans = float('-inf')
        freq={}

        for high in range (len(nums)):
            freq[nums[high]]= freq.get(nums[high],0)+1

            while(freq.get(0,0)>k): # if the freq of 0 is greater than k in window then shrink the window to fit 
                freq[nums[low]]=freq[nums[low]]-1
                if freq[nums[low]]==0:
                    del freq[nums[low]]
                low = low + 1
            length = high -low + 1 
            ans = max(ans,length)
        return 0 if ans == float('-inf') else ans 


