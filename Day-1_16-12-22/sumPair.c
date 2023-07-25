#include <stdio.h>

int main()
{
    int arr[]={8,7,9,6,5,3,10};
    int i,j,target =15;
    int size = sizeof(arr);
    for(i=0;i<size;i++)
    {
        for(j=i+1;j<size;j++)
        {
            if(arr[i]+arr[j]==target)
            {
                printf("Pair found at index %d and %d (%d,%d)",i,j,arr[i],arr[j]); 
            }
        }
    }
    
}
