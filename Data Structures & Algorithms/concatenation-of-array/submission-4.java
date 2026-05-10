class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = Arrays.copyOf(nums, nums.length*2);
        int count = nums.length;
        for(int i = 0; i < nums.length;i++) {
            ans[count] = nums[i];
            count++;
        }

        return ans;
    }
}