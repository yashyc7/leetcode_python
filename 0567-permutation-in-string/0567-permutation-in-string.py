class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #same as the minimum windows substring quesiton 
        low = 0 
        freq_s1={}
        freq_s2 = {}

        anwer = False 
        

        #store the charcters for s1 
        for ch in s1 : 
            freq_s1[ch]=freq_s1.get(ch,0)+1

        for high in range(len(s2)): 

            #calculate information and include the high in it 
            freq_s2[s2[high]]=freq_s2.get(s2[high],0)+1


            while(high-low+1> len(s1)):
                
                # wrong information then shrink the window 
                freq_s2[s2[low]]-=1
                if freq_s2[s2[low]]==0: 
                    del freq_s2[s2[low]]
                low = low+1

            # check if both maps are equal
            if freq_s2 == freq_s1:
                return True
        return False

            


