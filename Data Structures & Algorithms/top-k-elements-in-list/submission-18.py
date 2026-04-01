class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_mp = defaultdict(int)
        for n in nums:
            count_mp[n] += 1

        if len(count_mp.keys()) <= k:
            return list(count_mp.keys())

        # inverse
        inverse_mp = defaultdict(list)
        for key, val in count_mp.items():
            inverse_mp[val] += [key]

        sorted_keys = sorted(inverse_mp.keys(), reverse=True)

        res = []
        for i in range(k):
            print(res)
            for x in inverse_mp[sorted_keys[i]]:
                print(x)
                if len(res) == k:
                    return res
                res += [x]
                print(res)
        return res