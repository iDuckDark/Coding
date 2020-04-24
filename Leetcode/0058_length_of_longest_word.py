class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return len(s)
        array = s.split(" ")
        ptr = -1
        while len(array[ptr]) is 0:
            ptr -= 1
            if abs(ptr) == len(array) and len(array[ptr]) == 0:
                return 0
        return len(array[ptr])


solution = Solution()
sol = solution.lengthOfLastWord("Hello World ")
print(sol)
