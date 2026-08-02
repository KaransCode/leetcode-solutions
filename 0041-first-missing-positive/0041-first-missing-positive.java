class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            s.add(num);
        }
        for (int i = 1; i <= Integer.MAX_VALUE; i++) {
            if (!s.contains(i))
                return i;
        }
        return -1;
    }
}