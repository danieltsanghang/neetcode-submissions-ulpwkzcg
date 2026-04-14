class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = 0, len(matrix[0])-1
        while r <= len(matrix)-1 and c >= 0:
            mid = matrix[r][c]
            print(r,c,mid)
            if target == mid:
                return True
            elif target > mid:
                r += 1
            else:
                c -= 1
        return False
