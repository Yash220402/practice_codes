#include <iostream>
using namespace std;

int main() {
	
	int i,n; cin >> n;
	int a[n+1];  // +1 for our understanding of the base value
	for (i=1; i<=n; i++) { cin >> a[i]; }
	
	int j,m; cin >> m;
	int b[m+1];
	for (j=1; j<=n; j++) { cin >> b[j]; }
	
	int memo[n+1][m+1], max=0;
	
	for (i=0; i<=n; i++) {
		for (j=0; j<=m; j++) {
			if (i==0 || j==0) memo[i][j]=0;
			else if (a[i]==b[j]) memo[i][j] = memo[i-1][j-1] + 1;
			else memo[i][j] = 0;
			
			if (max < memo[i][j]) max = memo[i][j];
		}
	}
	cout << max;
	
	return 0;
}
