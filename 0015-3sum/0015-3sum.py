class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-2) :

            j = i+1 #put two inner pointers 
            k = len(nums)-1 

            if i>0 and nums[i]==nums[i-1]:
                continue
            while(j<k):
                current_sum = nums[i]+nums[j]+nums[k]

                if current_sum == 0:
                    ans.append([nums[i],nums[j],nums[k]])

                    while(j<k and nums[j]==nums[j+1]):
                        j=j+1
                    while(j<k and nums[k]==nums[k-1]):
                        k = k-1
                    j = j+1
                    k = k-1
                elif current_sum<0:
                    j = j+1
                else :
                    k = k-1
        return ans
