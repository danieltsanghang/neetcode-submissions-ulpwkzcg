class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mp2 = defaultdict(int)
        res = set()
        # a+b+c=0
        # a+b=0-c
        # a=0-c-b
        # 
        for pos, n in enumerate(nums):
            for k,v in enumerate(nums):
                if k == pos:
                    continue
                mp2[(k,pos)] = -v - n
        for pos, n in enumerate(nums):
            for k,v in mp2.items():
                if pos in k:
                    continue
                if v - n == 0:
                    res.add(tuple(sorted([nums[k[0]], nums[k[1]], nums[pos]])))
                    print(res)


        return [[r[0], r[1], r[2]] for r in res]