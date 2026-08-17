class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # start from rotten fruits, traverse to fresh fruit
        if not grid:
            return 0
        
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        fresh_fruit = 0

        def bfs(queue):
            nonlocal res, fresh_fruit

            while queue and fresh_fruit > 0:
                queue_len = len(queue)

                for _ in range(queue_len):
                    
                    node = queue.popleft()

                    for dr, dc, in directions:
                        r, c = node[0] + dr, node[1] + dc

                        if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                            grid[r][c] = 2
                            fresh_fruit -= 1
                            queue.append((r, c))

                res += 1

        # loading the queue with rotten oranges and counting the fresh oranges
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_fruit += 1

        bfs(queue)

        if fresh_fruit > 0:
            return -1

        return res 


        

