class Solution {
    public int numOfMinutes(int n, int head, int[] manager, int[] informTime) {
        List<List<Integer>> g = new ArrayList<>();
        while (g.size() < n) {
            g.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < n; i++) {
            if (manager[i] != -1) {
                g.get(manager[i]).add(i);
            }
        }
        int[] t = new int[n];
        Queue<Integer> q = new LinkedList<>();
        q.offer(head);

        int ans = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            if (g.get(u).isEmpty()) {
                ans = Math.max(ans, t[u]);
                continue;
            }
            for (int v : g.get(u)) {
                q.offer(v);
                t[v] = t[u] + informTime[u];
            }
        }
        return ans;
    }
}