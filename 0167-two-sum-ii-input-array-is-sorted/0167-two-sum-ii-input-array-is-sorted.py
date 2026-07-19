class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        high = len(numbers)-1
        low = 0
        while(low<high):
            current_sum = numbers[low]+numbers[high]
            if current_sum == target : 
                return [low+1,high+1]
            
            elif current_sum < target : 
                low = low + 1  #increment low will guarentee increase in current sum ( as the input array is sorted)
            else : 
                high = high - 1