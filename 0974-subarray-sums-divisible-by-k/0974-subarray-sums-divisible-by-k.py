class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # lets suppose running sum be the running_sum
        # and suppose result be as the res 
        # and suppose a hashmap to store the frequency of seen elements
        #hence 

        running_sum = 0 
        res = 0 
        freq = {0:1} # for empty subarray [] remainder is 0 mean 0%k == 0 so remainder 0 is seen only once 

        # looping and calculating running sum for indexes

        for i in range(len(nums)):
            running_sum += nums[i]
            #let rem be the remainer 
            rem = running_sum % k 

            if rem < 0 : #handeling the negative case 
                rem = rem+k
            # if we have seen this remainder before,
            if rem in freq:
                res += freq[rem]
                freq[rem] += 1
            else:
                freq[rem] = 1
        return res 

            