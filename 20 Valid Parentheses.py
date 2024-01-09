# 1st try, gave up
class Solution:
    def isValid(self, s: str) -> bool:
        for ch in s:
            if ch == "(":
                opposite = ")"
        return


# string always has to start with opening bracket
# hashmap to link type of bracket
# remove brackets as they match


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}": "{", "]": "[", ")": "("}
        # loop through string
        for ch in s:
            # if ch is a closing bracket
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            # if ch is an opening bracket
            else:
                stack.append(ch)

        return True if not stack else False
