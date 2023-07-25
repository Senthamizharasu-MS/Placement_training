#include <stdio.h>

int main()
{
    int n;
    printf("Enter a number : ");
    scanf("%d",&n);
    
    if(n>0)
    {
        if(n&n-1)
        {
            printf("no");
        }
        else
        {
            printf("yes");
        } 
    }
    else
    {
        printf("no");
    }
    
    return 0;
}
