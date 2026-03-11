class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        temp=""
        alpha="abcdefghijklmnopqrstuvwxyz1234567890"
        for i in s:
            if(i in alpha):
                temp+=i
        return (temp[::1]==temp[::-1])