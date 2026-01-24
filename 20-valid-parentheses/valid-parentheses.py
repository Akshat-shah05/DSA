class Solution:
    def isValid(self, s: str) -> bool:
        # Strat: put opening brackets on the stack, match w closing brackets
        stack = []
        matches = {")" : "(", "}" : "{", "]": "["}

        for par in s:
            if not stack and par in matches:
                return False
            
            elif par not in matches:
                stack.append(par)
            
            else:
                recent = stack[-1]
                if matches[par] == recent:
                    stack.pop()
                
                else:
                    return False
        
        return True if stack == [] else False
        