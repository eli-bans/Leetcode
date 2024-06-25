class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t,i])
        return res

# Time complexity: O(N), space complexity: O(N)

# 2. Brute force
# Time complexity: O(N^2), space complexity: O(1)

# The monotonous stack solution really got me confused ngl.
# The trick is to store the index of the temperature and the temperature itself in the stack.
# Somehow it works out such that if you keep popping values lower than your current temperature,
# you can calculate the difference between the indices to get the number of days.

#Maybe I do need more practice with stacks.