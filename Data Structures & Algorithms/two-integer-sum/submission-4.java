//import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
     //HashMap<Integer> map = new HashMap<Integer>();
     int difference = 0;
     int[] resu = new int[2];
    for(int i = 0; i < nums.length;i++) {
    difference = target - nums[i];
        for(int j = 0; j < nums.length;j++) {
            if(nums[j] == difference && i != j) {
            resu[0] = j;
            resu[1] = i;
            }
        }
    }
    return resu;
    }
}
