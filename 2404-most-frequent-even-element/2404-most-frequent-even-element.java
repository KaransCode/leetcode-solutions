class Solution {
    public int mostFrequentEven(int[] nums) {
        int ans=-1;
        Map<Integer,Integer> map=new HashMap<>();
        for(int num:nums){
            if(num%2==0){
                map.put(num,map.getOrDefault(num,0)+1);
            }
        }
        int max=Integer.MIN_VALUE;
        for(int i=(int) 1e5;i>=0;i-=2){
            if(map.containsKey(i)){
                if(max<=map.get(i)){
                    max=map.get(i);
                    ans=i;
                }
            }
        }
        return ans;
    }
}