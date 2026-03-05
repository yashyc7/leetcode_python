class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # we have non decreasing nums in array 
        # i am following two pointer approach here 
        #length of the array 
        n = len(nums)
        i = 0  # left pointer on nums array 
        j=n-1 # right pointer on nums array 

        result = [0]*n  # making dummy resultant array of same length as of input array 

        pos = n-1 # keeping the pointer on resultant array to start putting values from biggest ones


        while(i<=j):
            left_square = nums[i]**2#calculating the square of first element then same for right one
            right_square = nums[j]**2

            if left_square > right_square : 
                #If left element square is greater than right ones we are keeping the bigger ones as last as
                #on squaring we would get the biggest ones first
                result[pos]=left_square
                i=i+1 # incrementing the pointer 
            else : 
                #same for the right element 
                result[pos]=right_square
                j=j-1  # we decresase the pointer 
            pos = pos-1 # decrement the pointer on resultant array to fill up correct values 
        return result 
            
        