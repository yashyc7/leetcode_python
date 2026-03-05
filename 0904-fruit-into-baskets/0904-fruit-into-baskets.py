class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        # maximum means at most 

        left = 0 
        n = len(fruits)
        res = -1
        freq = {}

        for right in range (n):

            freq[fruits[right]] = freq.get(fruits[right],0)+ 1  # store the frequency of some element in the array

            while(len(freq) > 2): # while the 
                freq[fruits[left]] = freq[fruits[left]]-1 # decrease the frequency
                if freq[fruits[left]] == 0 : 
                    # delete the occurence in the dict
                    del  freq[fruits[left]]
                left = left + 1

            if len(freq) <=2:
                length = right - left + 1 
                res = max(length , res)

        return res 



             

                 
        