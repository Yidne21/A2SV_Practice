class Solution(object):

    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        sorted = [' '] * len(s)
        for word in s:
            index = int(word[-1])
            sorted[index - 1] = word[0:len(word) - 1]
            s = ' '.join(sorted)
        return s


solution = Solution()
s = input()
print(solution.sortSentence(s))