class MinStack:

    def __init__(self):
        # Initialize the main stack and the minimum stack
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the element onto the main stack
        self.main_stack.append(val)
        
        # Update the minimum stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the element from the main stack
        if self.main_stack:
            popped_element = self.main_stack.pop()
            
            # Update the minimum stack if needed
            if popped_element == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        if self.main_stack:
            return self.main_stack[-1]

    def getMin(self) -> int:
        # Return the minimum element from the minimum stack
        if self.min_stack:
            return self.min_stack[-1]

# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2
