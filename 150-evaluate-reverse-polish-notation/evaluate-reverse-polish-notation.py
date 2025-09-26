class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                stack.append(num1 + num2)

            elif token == "-":
                stack.append(num1 - num2)
        
            elif token == "*":
                stack.append(num1 * num2)

            elif token == "/":
                stack.append(int(num1 / num2))
        
            else:
                raise ValueError("Invalid Token")
        
        return stack[-1]