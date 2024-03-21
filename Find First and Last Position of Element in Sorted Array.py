class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    s = bisect_left(nums, target)
    if s == len(nums) or nums[s] != target:
      return -1, -1
    r = bisect_right(nums, target) - 1
    return s, r
