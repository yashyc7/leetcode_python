class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_ending = nums[0]
        final_answer = nums[0]

        for i in range(1,len(nums)):

            #starting from index 1 getting two versions of answers
            version_1 = nums[i]
            version_2 = best_ending + nums[i]

            #updating the best_ending here 

            best_ending = max(version_1 , version_2)

            # update the answer 
            final_answer = max(final_answer, best_ending)

        return final_answer 