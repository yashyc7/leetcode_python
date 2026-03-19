class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            j = i + 1
            k = n - 1

            while (j < k):

                target = nums[i] + nums[j] + nums[k]

                if target == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    j = j + 1
                    k = k - 1

                elif target < 0:
                    j = j + 1
                else:
                    k = k - 1

        # Fix: remove duplicates properly
        return list(map(list, set(map(tuple, ans))))