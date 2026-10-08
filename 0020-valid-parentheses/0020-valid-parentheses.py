class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {')':'(','}':'{',']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            # Change this to an 'elif' or 'if' block that handles the failure case
            elif s[i] in ')}]':
                # If stack is empty OR the top doesn't match, it's invalid
                if len(stack) == 0 or valid_dict[s[i]] != stack[-1]:
                    return False
                stack.pop()
                
        if len(stack)!=0:
            return False
        return True