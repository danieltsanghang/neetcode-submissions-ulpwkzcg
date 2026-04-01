class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a+b+c=0
        # a+b=0-c
        # a=0-c-b
        sorted_ = sorted(nums)
        res = set()
        mp = defaultdict(tuple)
        for pos, n in enumerate(sorted_):
            left_pos = 0
            right_pos = len(nums) - 1
            # if -n in mp.keys():
            #     print("added", (sorted_[pos], sorted_[mp[-n][0]], sorted_[mp[-n][1]]))
            #     res.add((sorted_[pos], sorted_[mp[-n][0]], sorted_[mp[-n][1]]))
            #     continue
            while left_pos < right_pos:
                mp[sorted_[left_pos] + sorted_[right_pos]] = (left_pos, right_pos)
                if pos == left_pos:
                    left_pos += 1
                    continue
                if pos == right_pos:
                    right_pos -= 1
                    continue
                t = n + sorted_[left_pos] + sorted_[right_pos]
                if t < 0:
                    left_pos += 1
                    continue
                elif t > 0:
                    right_pos -= 1
                    continue
                else:
                    res.add(tuple(sorted([sorted_[pos], sorted_[left_pos], sorted_[right_pos]])))
                    left_pos += 1
        return [list(r) for r in res]