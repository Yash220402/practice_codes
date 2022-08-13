#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	int a,b,i,j,c=0,x=0;
	char one[101] = "banana", two[101]="ana";
	
	//gets(one);
	//gets(two);
	
	a = strlen(one);
	b = strlen(two);
	
	if (a > b) {
		for (i=0; i<a; i++) 
		{
			for (i=0; j <i+b; j++) 
			{
				if (one[j] == two[j-i]) 
					c++;
				if (c==b) 
					x++;
				c=0;
			}
		}
	}
	else
	{
		for (i=0; i<b; i++) 
		{
			for (i=0; j <i+a; j++) 
			{
				if (two[j] == one[j-i])
					c++;
				if (c==b)
					x++;
				c=0;
			}
		}
	}
	printf("%d", x);
		
	return 0;
}
