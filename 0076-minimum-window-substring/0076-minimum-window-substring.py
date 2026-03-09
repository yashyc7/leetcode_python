class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        # first i wanted to initiate some variables 
        low = 0 
        freq_in_s = { } # map for string s
        freq_in_t = { } # map for string t
        matched = 0
        required = len(t)
        answer = float('inf')
        answer_high = 0 
        answer_low = 0

        for high in range(len(t)): 
            freq_in_t[t[high]]=freq_in_t.get(t[high],0)+1

        
        for high in range(len(s)): 
            # include the window information in hashmap
            freq_in_s[s[high]] = freq_in_s.get(s[high], 0) + 1

            # check if character contributes to match
            if s[high] in freq_in_t and freq_in_s[s[high]] <= freq_in_t[s[high]]:
                matched += 1

            # while information is correct shrink the window
            while matched == required:
                length = high - low + 1
                if length < answer:
                    answer = length
                    answer_low = low
                    answer_high = high

                # shrink the window
                freq_in_s[s[low]] -= 1

                if s[low] in freq_in_t and freq_in_s[s[low]] < freq_in_t[s[low]]:
                    matched -= 1

                # if no frequency is left delete character
                if freq_in_s[s[low]] == 0:
                    del freq_in_s[s[low]]

                low += 1

        if answer == float('inf'):
            return ""

        return s[answer_low:answer_high+1]