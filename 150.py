class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            # do for addition
            if i == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            # do for subtraction
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                # do for multiplication
            elif i == "*":
                a, b = stack.pop(), stack.pop()
                ans = b * a
                stack.append(ans)
                # do for division
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                ans = int(b / a)
                stack.append(ans)
                # add everything else to the stack
            else:
                stack.append(int(i))

        return stack[-1]

# Time complexity : O(n), Space complexity : O(n)
# Trick is to look out for the operators and perform the operations accordingly.