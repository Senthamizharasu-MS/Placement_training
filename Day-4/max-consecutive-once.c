int findMaxConsecutiveOnes(int* nums, int n){
int c=0,maxc=0;
for( int i=0;i<n;i++)
{
    if(nums[i]==1)
    {
        c++;
        if(c>maxc)
        {
            maxc=c;
        }
    }
    else
    {
        c=0;
    }
}
return maxc;
}