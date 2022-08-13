#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a,b,m;
    scanf("%d%d%d", &a,&b,&m);
    long x = 1;
    
    for(int i=b+1; i<=a; i++) 
        x = x*i%m;
    
    printf("%ld", x%m);
        
    return 0;
}

