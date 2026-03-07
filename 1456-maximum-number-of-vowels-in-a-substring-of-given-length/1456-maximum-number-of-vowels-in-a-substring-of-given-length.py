class Solution(object):

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # lets first count the number of the vowels in the first window 
        # lets make the frequency dict to keep track of the things 
        current_window_count = 0 
        vowels = ['a','e','i','o','u']
        for i in range(k):
            if s[i] in vowels :
                current_window_count+=1 
        max_window_count = current_window_count 
        for i in range (k , len(s) ): 
            #Remove old character
            if s[i] in vowels : 
                current_window_count += 1
            if s[i-k] in vowels : 
                current_window_count -=1 
            max_window_count = max(current_window_count , max_window_count )

        return max_window_count 
            

        