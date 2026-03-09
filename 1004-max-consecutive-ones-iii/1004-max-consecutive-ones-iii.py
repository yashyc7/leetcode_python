class Solution(object):
    def longestOnes(self, s, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        low = 0 
        zero_count= 0 
        ans= float('-inf')


        for high in range(len(s)): 

            if s[high]==0 : 
                zero_count += 1 
            while zero_count > k:

                if s[low] == 0:
                    zero_count -= 1

                low += 1

            # update maximum length
            ans = max(ans, high - low + 1)
        return ans