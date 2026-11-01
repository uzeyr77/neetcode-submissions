//import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
     HashMap<Integer,Integer> map = new HashMap<>();
     int[] resu = new int[2];
     // 3  0 
     // 4  1
     //

     for(int i = 0; i < nums.length;i++) {
        map.put(nums[i], i);
     }

     int difference = 0;

     for(int i = 0; i < nums.length;i++) {
        difference = target - nums[i];

            if(map.containsKey(difference) && map.get(difference) != i) {
                resu[0] = i;
                resu[1] = map.get(difference);
                return resu;
            }
     }


     return resu;
     

    }
}
