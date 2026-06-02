
"""
STEPS
Pre Reqs: dimensions, path set to maintain accepted elements/paths so far

1. get the dims of the board
2. declare a path set
3. define a nested dfs function
4. Accept case: when i reaches the end of the word. RETURN TRUE
5. Reject cases: if r or c are out of bounds. 
                 if word[i] doesnt match board[r][c]
                 if (r,c) already in path set
                RETURN FALSE
6. add (r,c) into the path
7. do dfs on 4 directions while incrementing i as well. Store val in res variable.
8. run nested for loops to do the dfs on each element of board.
9. return true if dfs is true. return false if the loop exits.
"""
from typing import List
class solution:
    def exists(self,board: List[List[str]],word: str)->bool:
        rows,cols=len(board),len(board[0])
        path=set()

        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or
                r>=rows or c>=cols or
                word[i]!=board[r][c] or
                (r,c) in path):
                return False
            path.add((r,c))

            res=(dfs(r+1,c,i+1) or
                 dfs(r-1,c,i+1) or
                 dfs(r,c+1,i+1) or
                 dfs(r,c-1,i+1)) 
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
    
class main:
    def main():
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]

        word = "ABCCED"

        sol = solution()
        print(sol.exists(board, word))




    if __name__=="__main__":
        main()