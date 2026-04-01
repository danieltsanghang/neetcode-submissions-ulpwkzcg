class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {v:k for k,v in enumerate(position)}
        s = []
        sorted_pos = list(sorted(mp.keys(), reverse=True))
        for pos in sorted_pos:
            if not s:
                s.append(pos)
            else:
                ahead = s[-1]
                ahead_sp = speed[mp[ahead]]
                ahead_steps = (target - ahead) / ahead_sp
                
                sp = speed[mp[pos]]
                steps = (target - pos) / sp
                if steps > ahead_steps:
                    s.append(pos)
        return len(s)
