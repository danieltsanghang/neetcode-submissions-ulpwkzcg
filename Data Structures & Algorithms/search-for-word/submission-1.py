class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width, height = len(board[0]), len(board)
        tmp = word
        for y in range(height):
            for x in range(width):
                letter = board[y][x]
                if letter != word[0]:
                    continue
                if len(word) == 1:
                    return True
                if dfs(width, height,board, y, x, set((y,x)), word):
                    return True
        return False

def dfs(w, h, board, y, x, visited, word)->bool:
    if 0 > y  or y >= h or 0 > x or x >= w:
        return False
    if board[y][x] == word[0] and (y,x) not in visited:
        if len(word) == 1:
            return True
        else:
            visited.add((y,x))
            res = (dfs(w,h,board, y+1, x, visited, word[1:]) or dfs(w,h,board, y-1, x, visited, word[1:]) or dfs(w,h,board, y, x+1, visited, word[1:]) or dfs(w,h,board, y, x-1, visited, word[1:]))
            visited.remove((y,x))
            return res
    else:
        return False

    
