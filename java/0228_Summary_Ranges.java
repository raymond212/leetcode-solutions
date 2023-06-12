class Solution {
    public List<String> summaryRanges(int[] nums) {
        int n = nums.length, i = 0;
        List<String> ans = new ArrayList<>();

        while (i < n) {
            int cur = nums[i];
            while (i + 1 < n && nums[i + 1] - nums[i] == 1) {
                i++;
            }

            if (nums[i] != cur) {
                ans.add(cur + "->" + nums[i]);
            } else {
                ans.add(String.valueOf(cur));
            }

            i++;
        }

        return ans;
    }
}