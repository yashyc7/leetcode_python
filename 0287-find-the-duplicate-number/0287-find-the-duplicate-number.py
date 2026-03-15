class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #
        slow =  0
        fast = 0 # both start at first index 

        while(True): # its guarenteed loop and duplicate numbers 
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast : 
                #loop found then fix the slow at the first index and then let fast there and increase by one 
                slow = 0 #fix slow at first 
                while(slow!=fast):
                    slow = nums[slow]
                    fast = nums[fast] #same logic as the start point of the loop
                return slow 
        return -1