class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracketDict = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in bracketDict.values(
            ):  # check if b is an opening bracket. if it isn't append it to the stack
                stack.append(b)
            elif b in bracketDict.keys(
            ):  # check if b is a closing bracket. if it is check the stack is not empty and there a match opening bracket on the stack
                if not stack or bracketDict[b] != stack.pop():
                    return False
            else:
                return False
        if stack:  # check the stack is empty or not
            return False
        return True


solution = Solution()
s = input()
print(solution.isValid(s))