class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if board[0][0] != -1:
            return -1
            
        n = len(board)
        visited = set()

        # Grid number translating to row and column
        def get_coordinates(sq_number):
            r = (sq_number-1)//n
            c = (sq_number-1)%n

            if r%2 == 0:
                return n-r-1, c
            return n-r-1, n-c-1

        queue = [(1,0)]

        # BFS - using a queue to add all the potential paths to traverse from that node.
        while queue:
            curr, moves = queue.pop(0)
            if curr == n*n:
                return moves
            
            for i in range(curr+1, min(curr+6, n*n)+1):
                if i not in visited:
                    visited.add(i)
                    r, c = get_coordinates(i)
                    if board[r][c]!=-1:
                        queue.append((board[r][c], moves+1))
                    else:
                        queue.append((i,moves+1))
        return -1