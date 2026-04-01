class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        box_check = defaultdict(set)

        for r, row in enumerate(board):
            for c, n in enumerate(row):
                if n == '.':
                    continue
                box = (self.findBox(r), self.findBox(c))
                print(box, n)
                if n in row_check[r] or n in col_check[c] or n in box_check[box]:
                    print(row_check)
                    print(col_check)
                    print(box_check)
                    print(n)
                    return False
                row_check[r].add(n)
                col_check[c].add(n)
                box_check[box].add(n)
        return True
    def findBox(self, pos:int) -> int:
        if pos < 3:
            return 0
        elif pos < 6:
            return 1
        else:
            return 2