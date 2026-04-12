class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # its an fixed window question we must make an answer array first
        k=len(p)
        ans = []

        first_window = s[:k]
        freq_p={} #track the freq of p 
        freq_s={} #track the freq of s

        for i in range (len(p)):
            freq_p[p[i]]=freq_p.get(p[i],0)+1
        
        # now for first window we are doing 
        for i in range(len(first_window)):
            freq_s[first_window[i]] = freq_s.get(first_window[i],0)+1

        if freq_s == freq_p:
            ans.append(0)
        
        for i in range(k,len(s)):
            # add new char
            freq_s[s[i]]=freq_s.get(s[i],0)+1

            #old char 
            left_char = s[i-k]
            freq_s[left_char]= freq_s[left_char]-1

            #also check if freq is 0 then delete 
            if freq_s[left_char]==0:
                del freq_s[left_char]

            if freq_s == freq_p:
                ans.append(i-k+1) # if i is the right bounday then i-k+1 is the starting element 
        return ans

        