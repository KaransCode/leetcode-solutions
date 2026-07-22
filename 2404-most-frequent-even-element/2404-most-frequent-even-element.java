class Solution {
    public int mostFrequentEven(int[] nums) {
        int n=(int) 1e5;
        int ans=-1;
        int[] map=new int[n+1];
        for(int num:nums){
            if(num%2==0){
                map[num]++;
            }
        }
        int max=Integer.MIN_VALUE;
        for(int i=n;i>=0;i--){
            if(map[i]>=max && map[i]!=0){
                max=map[i];
                ans=i;
            }
        }
        return ans;
    }
}