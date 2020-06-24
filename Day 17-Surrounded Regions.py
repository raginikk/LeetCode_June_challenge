class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        if m<=1:
            return
        n=len(board[0])
        moves = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(i, j):
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j]='E'
                for p,q in moves:
                    dfs(i+p,j+q)
			
        for i in range(m):
            for j in range(n):
                if i==0 or i==(m-1) or j==0 or j==(n-1) and board[i][j]=='O':
                    dfs(i,j)
        board[:] = [['XO'[c=='E'] for c in row] for row in board]

        
