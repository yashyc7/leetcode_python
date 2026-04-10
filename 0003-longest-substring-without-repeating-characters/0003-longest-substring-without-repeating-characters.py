class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #if the length of the longest substring is asked then now 
        # without duplicate meaning each character has exactly one occurence 
        # hence length of the hashmap should be equal to the length of the current_window 


        low = 0 
        freq = { }
        ans = 0


        for high in range(len(s)): 

            # include information in window 

            freq[s[high]] = freq.get(s[high], 0) + 1

            while (len(freq)<high-low+1): #since high-low+1 is the answer to be returned uuntill this is incorrect we would shrink 
                freq[s[low]]=freq[s[low]]-1 #shrink then outside while update ans 

                if freq[s[low]]==0:
                    del freq[s[low]]
                
                low = low + 1

            if len(freq)==(high-low+1): # update answer with information is right check 
                ans = max(ans,high-low+1)

        return ans