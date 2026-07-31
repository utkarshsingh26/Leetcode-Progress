class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        sett = {"+", "-", "/", "*"}

        for token in tokens:
            if token not in sett:
                stack.append(token)
            else:
                
                first_num = int(stack.pop())
                second_num = int(stack.pop())

                if token == "+":
                    result = str(first_num + second_num)
                elif token == "-":
                    result = str(second_num - first_num)
                elif token == "*":
                    result = str(first_num * second_num)
                elif token == "/":
                    result = str(int(second_num / first_num))

                stack.append(result)

        return int(stack[0])