class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #it just only means that len(freq) is equal to the length of the window 
        # THIS Proves that every character has only one occurence 

        low = 0
        ans = float('-inf')
        freq = {}

        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1

            while(freq[s[high]]>1) :
                freq[s[low]]=freq[s[low]]-1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low = low + 1
            length = high - low + 1
            ans = max(ans,length)
        return 0 if ans == float('-inf') else ans 
