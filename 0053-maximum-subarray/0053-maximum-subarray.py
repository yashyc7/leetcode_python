class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_ending = nums[0]
        answer = nums[0]
        
        for i in range (1,len(nums)):
            var_1 = nums[i]
            var_2 = best_ending + nums[i]

            # update the previous best ending at the known i-1 place 
            best_ending = max(var_1,var_2)

            # update the answer 
            answer = max(answer, best_ending)

        return answer 