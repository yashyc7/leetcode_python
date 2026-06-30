class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # total represents the running prefix sum
        total = 0

        # count stores the number of valid subarrays found
        count = 0

        # freq stores:
        # prefix_sum -> number of times it has appeared
        #
        # We initialize {0:1} because before starting,
        # there is one prefix sum of 0.
        # This helps handle cases where a subarray starting
        # from index 0 itself has sum = k.
        freq = {0: 1}

        for num in nums:

            # keep calculating the running prefix sum
            total += num

            # We know:
            #
            # current_prefix_sum - previous_prefix_sum = k
            #
            # therefore:
            #
            # previous_prefix_sum = current_prefix_sum - k
            #
            # If (total - k) has appeared before, then every
            # occurrence represents a valid subarray ending
            # at the current index.
            count += freq.get(total - k, 0)

            # Store the current prefix sum in the hashmap
            # so future elements can use it.
            freq[total] = freq.get(total, 0) + 1

        return count