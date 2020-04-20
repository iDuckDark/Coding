# A password is considered strong if below conditions are all met:
#
# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a
# row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
# Write a function strongPasswordChecker(s), that takes a string s
# as input, and return the MINIMUM change required to make s a
# strong password. If s is already strong, return 0.
# Insertion, deletion or replace of any one character are all considered as one change.

import re


class Solution:

    #  takes in the string, outputs a list of runs of
    #  a single character of 3 or more
    #  ex: "aaaaabbbbbbccdeeee" -> [5,6,4]
    def lengthCheck(self, s):
        l = []
        curr = 1
        for i in range(1, len(s)):
            if s[i] is s[i - 1]:
                curr += 1
            else:
                if curr > 2: l.append(curr)
                curr = 1
        if (curr > 2): l.append(curr)
        return l

    # return 1 if we are missing an uppercase
    def uppercaseCheck(self, s):
        return 1 if re.search("[A-Z]", s) is None else 0

    # return 1 if we are missing a lowercase
    def lowercaseCheck(self, s):
        return 1 if re.search("[a-z]", s) is None else 0

    # return 1 if we are missing a number
    def numberCheck(self, s):
        return 1 if re.search("[0-9]", s) is None else 0

    def strongPasswordChecker(self, s: str) -> int:
        leng = len(s)

        # If the password is 3 or less, then there is always a way
        # to just add characters until it is length 6 and make a
        # strong password
        if leng <= 3:
            return 6 - leng

        if leng == 4:
            if self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 3:
                return 3
            return 2

        # For length 5, we only need to add 2 characters
        # if we are missing two types
        # 3 characters if missing all types
        if leng == 5:
            if self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 3:
                return 3
            if self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 2:
                return 2
            return 1

        lis = self.lengthCheck(s)

        # If the length is acceptable, then all the changes can be replacements.
        # We need to make replacements to eliminate runs
        # ex: aaaaaaaa -> aaxaaxaa
        # hence the quotient by 3 rounded down.
        # If that number is lower than the missing types
        # then take the missing types
        if leng <= 20:
            return max(sum(map(lambda x: int(x / 3), lis)),
                       self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s))

        # for too long passwords...
        if leng > 20:
            # we first count how many deletions we need
            numdel = leng - 20

            # the amount of replacements due to runs we would need
            # is reduced by the deletions
            runreplace = sum(map(lambda x: int(x / 3), lis))

            # order the runs by how many deletions needed
            # to eliminate one replacement
            # ex. aaa needs 1 deletion, aaaa needs 2, aaaaa needs 3
            l = list(map(lambda x: (x % 3) + 1, lis))
            l.sort()

            # variable to keep track of how many deletions are left
            rem = numdel

            # first the cheap ones:
            # aaa -> aa is one deletion to save one replacement
            for i in range(0, len(l)):
                if rem >= l[i]:
                    rem -= l[i]
                    runreplace -= 1

            # after the cheap ones, take the most expensive ones
            # ex aaaaa -> aa saves 1 replacement, aaaaaaaa -> aa saves 2 replacements.
            # This calculation might make runreplace negative
            runreplace -= int(rem / 3)

            # if we need more replacements due
            # to the checks (or runreplace is negative)
            # make the number of replacements correct
            if (runreplace < self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(
                    s)):
                runreplace = self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s)

            # total changes
            return numdel + runreplace
        return 0


solution = Solution()
minimum = solution.strongPasswordChecker("")
print(minimum)
