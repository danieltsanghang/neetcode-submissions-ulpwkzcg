class Solution:

    def encode(self, strs: List[str]) -> str:
        # res = ''
        # for s in strs:
        #     res += ']n' + s
        # return res
        if len(strs) == 0:
            return "."
        return '\n'.join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == ".":
            return []
        return s.split('\n')
