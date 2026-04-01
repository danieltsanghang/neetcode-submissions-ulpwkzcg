class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for n in nums]
        right = [1 for n in nums]
        # left = [1, 1*1, 1*1*2, 1*1*2*4]
        # (reversed) right = [2*4*6, 4*6, 6, 1]
        # res = [0][0]
        for pos, n in enumerate(nums):
            if pos == 0:
                left[pos] = 1
            else:
                left[pos] = left[pos-1] * nums[pos-1]

            r = len(nums) - pos - 1
            if r == len(nums)-1:
                right[r] = 1
            else:
                right[r] = right[r+1] * nums[r+1]
            print(left, right)

        return [left[i] * right[i] for i in range(len(nums))]