class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        left = 0
        max_freq = 0
        res = 0

        for right in range(len(s)):
            # include character in window
            freq[s[right]] = freq.get(s[right], 0) + 1

            # update most frequent character count
            max_freq = max(max_freq, freq[s[right]])

            # check if window invalid
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # update result
            res = max(res, right - left + 1)

        return res