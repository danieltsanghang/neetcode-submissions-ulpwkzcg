class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)-1
        if N < 3:
            return max(nums)
        a = robLinear(nums[1:])
        b = robLinear(nums[:-1])
        return max(a,b)

def robLinear(nums):
        N = len(nums)
        possible = [0] * (N+1)
        possible[N-1] = nums[N-1]
        for i in range(N-2, -1, -1):
            cur = nums[i]
            possible[i] = max(cur + possible[i+2], possible[i+1])
        return max(possible)