class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        s = 0
        for j, x in enumerate(nums):
            i = bisect_left(nums, target - x, hi=j)
            s += i
        return s
