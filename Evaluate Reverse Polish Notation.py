class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens :
            if token == '+' :
                s , r = stack.pop() , stack.pop()
                stack.append( s + r ) 
            elif token == '-':
                s , r = stack.pop() , stack.pop()
                stack.append( r - s ) 
            elif token == '*':
                s , r = stack.pop() , stack.pop()
                stack.append( r * s ) 
            elif token == '/':
                s , r = stack.pop() , stack.pop()
                stack.append( int(r / s) ) 
            else:
                stack.append(int(token)) 
        return stack.pop()                   

        
