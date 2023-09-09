class Solution {
    public int romanToInt(String s) {
        int ans = 0;
        int length = s.length();

        Map<Character, Integer> mp = new HashMap<>();
        mp.put('I', 1);
        mp.put('V', 5);
        mp.put('X', 10);
        mp.put('L', 50);
        mp.put('C', 100);
        mp.put('D', 500);
        mp.put('M', 1000);

        for (int i = 0; i < length; i++) {
            if (i < length - 1 && mp.get(s.charAt(i + 1)) > mp.get(s.charAt(i))) {
                ans -= mp.get(s.charAt(i));
            } else {
                ans += mp.get(s.charAt(i));
            }
        }

        return ans;
    }
}