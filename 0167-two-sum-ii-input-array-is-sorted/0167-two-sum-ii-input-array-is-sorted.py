class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i = 0 
        j = n-1
        ans = [0]*2

        while(i<j):
            current_sum = numbers[i]+numbers[j]

            if (current_sum == target): # if index found then return the indexes  
                return [i+1,j+1]
            elif (current_sum<target):
                i = i+1
            else : 
                j = j-1

        return [-1,-1]
        