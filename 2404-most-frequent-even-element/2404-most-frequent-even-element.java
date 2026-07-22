class Solution {
    public int mostFrequentEven(int[] nums) {
        int ans=-1;
        Map<Integer,Integer> map=new TreeMap<>();
        for(int num:nums){
            if(num%2==0){
                map.put(num,map.getOrDefault(num,0)+1);
            }
        }
        int max=Integer.MIN_VALUE;
        for(int key:map.keySet()){
            if(max<map.get(key)){
                max=map.get(key);
                ans=key;
            }
        }
        return ans;
    }
}