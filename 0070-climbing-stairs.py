class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1

        one_up = 1
        two_up = 1
        total = 0

        for i in range(n-1):
            total = one_up + two_up
            two_up = one_up
            one_up = total

        return total
