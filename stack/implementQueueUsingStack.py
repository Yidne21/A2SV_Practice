class MyQueue(object):
    stack = []

    def __init__(self):
        self.inStack = [1]
        self.outStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.outStack and not self.inStack


x = int(input())
obj = MyQueue()
obj.push(x)
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.empty())
