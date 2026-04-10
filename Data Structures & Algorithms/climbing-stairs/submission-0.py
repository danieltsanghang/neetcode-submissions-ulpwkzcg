class Solution:
    def climbStairs(self, n: int, cur=0, memo=None) -> int:
        if memo is None:
            memo = [0] * (n+1)
        if cur > n:
            return 0
        if cur == n:
            return 1
        if memo[cur] > 0:
            return memo[cur]
        memo[cur] = self.climbStairs(n, cur+1, memo) + self.climbStairs(n, cur+2, memo)
        return memo[cur]