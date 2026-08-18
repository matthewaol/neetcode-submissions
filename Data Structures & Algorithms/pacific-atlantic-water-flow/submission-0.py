class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return heights
        rows, cols = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # prepopulate the set
        pac = set()
        atl = set()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pac.add((r, c))
                if r == rows - 1 or c == cols - 1:
                    atl.add((r, c))

        # we call the dfs on the nodes of the oceans
        def dfs(r, c, ocean):
            st = collections.deque()
            st.append((r, c))
            visited = set()

            while st:
                r, c = st.popleft()

                for dr, dc in directions: 

                    row, col = r + dr, c + dc

                    if row in range(rows) and col in range(cols) and (heights[row][col] >= heights[r][c] or (row, col) in ocean) and (row, col) not in visited:
                        visited.add((row, col))
                        st.append((row, col))
                        ocean.add((row, col))
        
        dfs(0, 0, pac)
        dfs(rows - 1, cols - 1, atl)
        
        # after dfs, then we go through each node on the grid, and if its in both then we append to result
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
