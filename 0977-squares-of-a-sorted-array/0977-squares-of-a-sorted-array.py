class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums)-1
        #taking array of size n 
        arr = [0]*len(nums) 

        pos = len(nums)-1

        while(i<=j):
            left_square  = nums[i]**2
            right_square = nums[j]**2 

            if left_square > right_square: 
                arr[pos]= left_square
                i  = i + 1
            else : 
                arr[pos] = right_square
                j = j - 1
            pos = pos - 1

        return arr 

        