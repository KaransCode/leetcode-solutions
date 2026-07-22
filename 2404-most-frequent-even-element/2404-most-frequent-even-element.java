class Solution {
    public int mostFrequentEven(int[] nums) {
        int m=Integer.MIN_VALUE;
        for(int num:nums){
            m=Math.max(m,num);
        }
        int ans=-1;
        int[] map=new int[m+1];
        for(int num:nums){
            if(num%2==0){
                map[num]++;
            }
        }
        int max=Integer.MIN_VALUE;
        for(int i=m;i>=0;i--){
            if(map[i]>=max && map[i]!=0){
                max=map[i];
                ans=i;
            }
        }
        return ans;
    }
}