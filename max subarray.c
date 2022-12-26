int maxSubArray(int* nums, int n) {
    if(n==1)
    {return nums[0];}
    int sum=nums[0];
    int result=sum;
    for(int i=0;i<n-1;i++)
    {
        if(sum<=0)
        {sum=0;}
        sum=sum+nums[i+1];
        if(result<sum)
        {result=sum;}
    }
    return result;
}
