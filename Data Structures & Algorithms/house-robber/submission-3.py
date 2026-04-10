class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        possible=[0]*(len(nums)+3)
        # [1,2,3,4,5,6,7]
        # [0,2->,3->3+max(12,6,7),4->4+max(6,7),5->5+7,6,7]
        future_max = [0] * 2
        for n in reversed(list(range(len(nums)))):
            # store current max at possible[n]
            if n+2 >= len(nums):
                possible[n] = nums[n]
                # print(nums[n], "a")
            else:
                # if n+3 >= len(nums):
                #     possible[n] = nums[n] + possible[n+2]
                possible[n] = max(nums[n] + possible[n+2], possible[n+1]) # add self to the max of +2 step or +3 steps
                # print(nums[n], "b", possible[n+2:])
            # print(possible)
            # print()
        return max(possible)