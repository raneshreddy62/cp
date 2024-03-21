class Solution:
  def search(self, nums: List[int], target: int) -> int:
    s = 0
    r = len(nums) - 1
    while s<= r:
      n = (s + r) // 2
      if nums[n] == target:
        return n
      if nums[s] <= nums[n]:  
        if nums[s] <= target < nums[n]:
          r = n - 1
        else:
          s = n + 1
      else:
        if nums[n] < target <= nums[r]:
          s = n + 1
        else:
          r = n - 1

    return -1
