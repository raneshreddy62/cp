class Solution:
    def customSortString(self, order: str, s: str) -> str:
        welcome=""
        ts={}
        for char in s:
            ts[char]=ts.get(char,0)+1
        for char in order:
            if char in ts:
                welcome+=char*ts[char]
                del ts[char]
        for char,count in ts.items():
            welcome+=char*count
        return welcome
