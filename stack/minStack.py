class MinStack(object):

    def __init__(self):
        self.stack = [1]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return min(self.stack)


val = int(input())
obj = MinStack()

obj.push(val)
print(obj.pop())
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)