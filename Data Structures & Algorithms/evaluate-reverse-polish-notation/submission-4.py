class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())

                match token:
                    case "+":
                        result = operand2 + operand1
                    case "-":
                        result = operand2 - operand1
                    case "*":
                        result = operand2 * operand1
                    case "/":
                        result = int(operand2 / operand1)
                    case _:
                        result = None
                stack.append(result)

        return int(stack[0])