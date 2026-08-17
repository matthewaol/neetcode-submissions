class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # go from treasure chest to land
        if not grid:
            return grid
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        inf = 2**31 - 1

        def bfs(queue):
            while queue:
                chest = queue.popleft()

                for dr, dc in directions:
                    r, c = dr + chest[0], dc + chest[1]

                    if r in range(rows) and c in range(cols) and grid[r][c] == inf:
                        grid[r][c] = grid[chest[0]][chest[1]] + 1 # what this distance calculation
                        queue.append((r, c))

        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        bfs(queue)

        return 

