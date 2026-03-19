class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        max_diff = float('inf')

        for i in range(n-2):
            j = i + 1 
            k = n - 1

            while(j<k):
                total = nums[i]+nums[j]+nums[k]
                diff = abs(target - total)
                if diff<max_diff :
                    max_diff = diff 
                    result = total

                if total < target  :
                    j = j+1 
                elif total == target :
                    # increase j 
                    j = j + 1 
                    # decrese k 
                    k = k - 1
                else :
                    k = k - 1
        return result 

                