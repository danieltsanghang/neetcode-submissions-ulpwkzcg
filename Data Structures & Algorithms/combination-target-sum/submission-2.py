class Solution:
    def combinationSum(self, nums: List[int], target: int, isSorted=False) -> List[List[int]]:
        ans = []
        # 16%3=1 16%4=0 16%5=6
        if not isSorted:
            nums.sort()
        for i, n in enumerate(nums):
            multiple = target//n
            reminder = target%n
            # print('n:',n, 'mul:', multiple, 're:', reminder)
            if multiple == 1 and reminder != 0 and reminder not in nums:
                continue
            if reminder == 0:
                # add answer where mutiples of n equals target
                # print('found exact match', n)
                ans.append([n]*multiple)
            for m in range(multiple-1): # n=4|target=12 gives: [4], [4,4], [4,4,4] <- this is already handled
                newTarget = target - ((m+1) * n)
                if newTarget < n:
                    # skip if new target is less then n, it won't be in the recursion
                    continue
                prefix = [n for _ in range(m+1)]
                tmp = self.combinationSum(nums[i+1:], newTarget, True) # since its sorted we only need to check the remaining values of nums
                # print('checked for prefix:', prefix, ' new target:', newTarget, ' result:', tmp)
                for x in tmp:
                    ans.append(prefix+x)
        return ans
