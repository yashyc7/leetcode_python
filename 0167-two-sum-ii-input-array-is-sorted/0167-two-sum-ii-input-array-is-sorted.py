class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        low = 0 
        high = len(nums)-1
        ans = []

        while(low<high):
            sums = nums[low]+nums[high]

            if sums==target:
                ans.append(low+1)
                ans.append(high+1)
                break
            if sums<target:
                low = low+1
            if sums>target: 
                high = high-1
        return ans
             
        