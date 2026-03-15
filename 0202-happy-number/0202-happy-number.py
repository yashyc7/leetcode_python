class Solution:
    def calculate_sum(self,n:int)-> int :
        sum = 0
        while(n>0):
            digit = n % 10
            n = n // 10
            sum = sum + digit * digit 
        return sum 
    
    def isHappy(self, n: int) -> bool:

        slow = n 
        fast = n 

        while((fast)!=1):   
            # move slow pointer 1 time and fast pointer two times 
            slow = self.calculate_sum(slow)
            fast = self.calculate_sum(self.calculate_sum(fast))
            if( slow == fast and (slow)!=1 ):
                return False 
        return True