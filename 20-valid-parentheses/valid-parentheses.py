class Solution:
    def isValid(self, s: str) -> bool:
        allowed = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char not in allowed:
                stack.append(char)
        
            elif stack and allowed[char] == stack[-1]:
                stack.pop()

            else:
                return False
        
        return True if not stack else False
        
