class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if (len(set(nums))==len(nums)): # set will discard the duplicate element from the list and hence after that we can check wheather the length of the initial list is equal to the length of the converted set 
            return False
        return True
        