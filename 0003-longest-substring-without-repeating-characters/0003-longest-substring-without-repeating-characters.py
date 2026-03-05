class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # logic is len(freq)== size of the window  then it would be the longest substring 
        # mean the all elements has equal occurence 
        left = 0
        n = len(s)
        freq = {}
        res = 0

        for right in range(n):

            freq[s[right]] = freq.get(s[right], 0) + 1

            while (right - left + 1) > len(freq):
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            length_of_window = right - left + 1
            res = max(res, length_of_window)

        return res