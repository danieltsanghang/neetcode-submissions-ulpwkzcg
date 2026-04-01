class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # input will always be increasing timestamp so its inheritly sorted
        self.mp[key] += [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            print("key not in mp")
            return ""
        elif self.mp[key][0][0] > timestamp:
            print("existing keys are larger then ", timestamp)
            return ""
        else: 
            x = self.mp[key]
            l, r = 0, len(x) - 1
            while l <= r:
                c = (l+r) // 2
                print(c, x[c])
                if x[c][0] == timestamp:
                    return x[c][1]
                if x[c][0] > timestamp:
                    print("moved right bound")
                    r = c - 1
                else:
                    print("moved left bound")
                    l = c + 1
            print("converged onto", x[r], '\n')
            return x[r][1]

        
