class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {")": "(", "}":"{", "]": "["}

        for b in s:
            if b in mp:
                if stack and stack[-1] == mp[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False

        