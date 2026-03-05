class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]: # terminate duplicates 
                continue

            for j in range (i+1,  n -2):
                if j>i+1 and nums[j]==nums[j-1]: # also terminate the duplicates here too 
                    continue 

                left = j+1
                right = n-1

                while(left<right): 
                    current_sum = nums[i]+nums[j]+nums[left]+nums[right]

                    if current_sum == target :
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        # terminate duplicates here too . 
                        while left < right and nums[left]== nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                        
                    elif current_sum<target : 
                        left+=1
                    else : 
                        right-=1
        return ans

