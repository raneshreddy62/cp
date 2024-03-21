class Solution:
    def twoSum(self,nums,target):
        ranesh={}
        r=0
        while r<len(nums):
            num=nums[r]
            chennai=target-num
            if chennai in ranesh:
                return[r,ranesh[chennai]]
            ranesh[num]=r
            r+=1
