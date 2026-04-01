class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {v:k for k,v in enumerate(position)}
        s = []
        sorted_pos = list(sorted(mp.keys(), reverse=True))
        for pos in sorted_pos:
            if not s:
                s.append(pos)
            else:
                cur = s[-1]
                cur_sp = speed[mp[cur]]
                cur_steps = (target - cur) / cur_sp
                
                sp = speed[mp[pos]]
                steps = (target - pos) / sp
                if steps > cur_steps:
                    s.append(pos)
        return len(s)
        # for pos in sorted_pos[1:]:
        #     sp = speed[mp[pos]]
        #     iterations = int((target - pos) / sp)
        #     if not s:
        #         s.append(pos + sp * iterations)
        #     else:
        #         cur = pos
        #         while cur+sp <= s[-1]:
        #             cur += sp
        #         s.append(cur)
        #     print(s)
        return len(set(s))
