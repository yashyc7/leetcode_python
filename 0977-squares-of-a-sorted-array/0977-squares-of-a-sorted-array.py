class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = len(nums) * [0]
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        # now the array becomes
        # [16 , 1 , 0 , 9 , 100 ]

        left = 0
        right = len(nums) - 1
        pos = len(ans) - 1

        # last se bharna shuru karte hain
        while left <= right:
            if nums[left] > nums[right]:
                ans[pos] = nums[left]
                left = left + 1
            else:
                ans[pos] = nums[right]
                right = right - 1
            pos = pos - 1

        return ans
