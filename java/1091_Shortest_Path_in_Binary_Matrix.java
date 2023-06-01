class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
            return -1;
        }
        
        int[][] dirs = {{0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}};

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        int ans = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            ans++;
            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                if (cur[0] == n - 1 && cur[1] == n - 1) {
                    return ans;
                }
                for (int[] dir : dirs) {
                    int nr = cur[0] + dir[0];
                    int nc = cur[1] + dir[1];
                    if (nr < 0 || nr >= n || nc < 0 || nc >= n || grid[nr][nc] == 1) {
                        continue;
                    }
                    grid[nr][nc] = 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }

        return -1;
    }
}