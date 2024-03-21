class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        s=sorted(prices)
        return(money-s[0]-s[1] if s[0]+s[1]<=money else money)
        
