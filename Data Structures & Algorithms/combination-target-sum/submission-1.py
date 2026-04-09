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
                # print('found exact match', n)
                ans.append([n]*multiple)
            for m in range(multiple-1):
                newTarget = target - ((m+1) * n)
                if newTarget < n:
                    continue
                prefix = [n for _ in range(m+1)]
                tmp = self.combinationSum(nums[i+1:], newTarget, True)
                # print('checked for prefix:', prefix, ' new target:', newTarget, ' result:', tmp)
                for x in tmp:
                    ans.append(prefix+x)
        # add feq map to dedupe
        return ans
