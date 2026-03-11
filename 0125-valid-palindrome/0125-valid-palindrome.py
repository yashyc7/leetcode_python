class Solution(object):
    def isPalindrome(self, string):
        """
        :type s: str
        :rtype: bool
        """
        #now checking if the string is pallindrome or not

        cleaned_string = ''.join( c.lower() for c in string if c.isalnum())

        return cleaned_string== cleaned_string[::-1] 