class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Edge case: if k <= 1, no positive product can be less than k
        if k <= 1:
            return 0

        low = 0
        product = 1   # multiplication identity
        count = 0

        for high in range(len(nums)):

            # Expand window
            product *= nums[high]

            # Shrink window if product becomes invalid
            while product >= k:
                product //= nums[low]
                low += 1

            # Count all valid subarrays ending at high
            count += (high - low + 1)

        return count