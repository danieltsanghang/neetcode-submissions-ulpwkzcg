class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height, width = len(matrix) ,len(matrix[0])
        l, r = 0, height * width
        
        while l < r:
            c = (l + r) // 2
            cur = matrix[c // width][c % width]
            print(c, cur)
            if cur == target:
                return True
            elif cur < target:
                l = c + 1
            else:
                r = c
        return False
