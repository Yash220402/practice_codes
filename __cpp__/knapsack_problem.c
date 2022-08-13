/*
KNAPSACK PROBLEM
You are given an empty bag that is supposed to be filled with gold, 
and it can carry at max W kgs of gold in it.

You are given N samples of gold, with the ith of them weighing Wi 
and having value Vi.

Your task is to fill the bag with exactly W kgs of gold such that 
the total value of the gold inside the bag is maximum.

You need not take the entire samples of gold, you can break them down 
and take fractions of those samples as well. For example, if you have 
two samples, one with weight 10 and value 10 and another with weight 5 
and value 10, you can fill a 5 kg capacity bag with 2.5 kg of first 
sample and 2.5 kg of second sample. The value for such a bag will be 
the sum of values of all the pieces, i.e. for the first sample 2.5 kg 
has value 2.5 and for the second sample 2.5 kg has value 5, hence the 
total value of the bag becomes 7.5
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct  bag {
	double w,p,r;
};

int cmp (struct bag *a, struct bag *b) {
	if (b->r > a->r) return 1;
	else if (b->r < a->r) return -1;
	else return 0;
}

int main() {
	int n, m;
	scanf("%d%d", &n,&m);
	
	struct bag a[n];
	
	for(int i=0; i<n; i++) {
		scanf("%lf%lf", &a[i].w, &a[i].p);
		a[i].r=a[i].p/a[i].w;
	}
	
	qsort(a, n, sizeof(struct bag), cmp);
	double profit = 0;
	int i = 0;
	
	while(i<n && a[i].w<m) {
		profit = profit + a[i].p;
		m = m - a[i].w;
		i++;
	}
	if (i<n && m>0) {
		profit = profit + m *a[i].r;
	}
	
	if (i==n && m>0) 
		{ printf("-1"); }
	else 
		{ printf("%.12lf", profit); }
	
	return 0;
}
