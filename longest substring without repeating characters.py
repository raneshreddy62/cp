class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        finish=result=0
        ranesh={}
        for i, letter in enumerate(s):
            if ranesh.get(letter,-1) >=finish:
                finish=ranesh[letter]+1
            result=max(result,i-finish+1)
            ranesh[letter]=i
        return result 
