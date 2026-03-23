class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ""
        #cleaning string 
        for i in s:
            if i.isalnum():
                cleaned_str  = cleaned_str+i.lower()

        i =  0
        j = len(cleaned_str)-1

        while(i<j):
            if cleaned_str[i]!=cleaned_str[j]:
                return False
            i=i+1
            j=j-1
        return True