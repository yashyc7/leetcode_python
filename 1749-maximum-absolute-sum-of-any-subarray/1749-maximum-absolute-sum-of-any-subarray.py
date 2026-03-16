class Solution:
    def maxAbsoluteSum(self, arr: List[int]) -> int:

        best_ending = arr[0]
        worst_ending = arr[0]

        ans = abs(arr[0])

        for i in range(1, len(arr)):

            v1 = arr[i]
            v2 = best_ending + arr[i]
            v3 = worst_ending + arr[i]

            # update best positive sum
            best_ending = max(v1, v2)

            # update worst negative sum
            worst_ending = min(v1, v3)

            # update answer
            ans = max(ans, abs(best_ending), abs(worst_ending))

        return ans