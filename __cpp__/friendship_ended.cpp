#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to 
	STDOUT */    
    char s[] = {'G','o','o','d','b','y','e', '\0'};
    char t[500]; scanf("%s", t);
    
    int sz = strlen(s), tz = strlen(t), i=0, j=0;
    
    while (i < sz && j < tz) {
        if (s[i]==t[j]) {
            i++;
            j++;
        }
        else { j++; }
    }
    
    i == sz?printf("Yes"):printf("No");
    
    return 0;
}
