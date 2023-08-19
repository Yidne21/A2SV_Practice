import math


class Solution(object):

    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                s = s[:j] + s[j + 1:i][::-1] + s[i + 1:]
                # Remove the brackets and concatenate the modified substring
                return reverseParentheses(s) if '(' in s else s


# '(oc)'
# '(et(oc)el)'
# '(ed(et(oc))el)'

obj = Solution()
s = input()
obj.reverseParentheses(s)