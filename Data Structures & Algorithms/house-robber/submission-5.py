class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        N = len(nums)
        possible=[0] * (N+1)
        # [1,2,3,4,5,6,7]
        # [0,2->,3->3+max(12,6,7),4->4+max(6,7),5->5+7,6,7]
        possible[N], possible[N-1] = 0, nums[N-1]
        for n in range(N-2, -1, -1):
            print(n)
            # store current max at possible[n]
            possible[n] = max(possible[n+1], possible[n+2]+nums[n]) # add self to the max of +2 step or sip current and rob +1 steps
        return max(possible)