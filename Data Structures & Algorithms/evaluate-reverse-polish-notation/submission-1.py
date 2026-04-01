class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            print(s)
            if t in ['+', '-', '*', '/']:
                l = s[-2]
                r = s[-1]
                res = 0
                if t == '+':
                    res = l + r
                elif t == '-':
                    res = l - r
                elif t == '*':
                    res = l * r
                elif t == '/':
                    res = int(l / r)
                s = s[:-2] + [res] 
            else:
                s += [int(t)]
        return s[0]