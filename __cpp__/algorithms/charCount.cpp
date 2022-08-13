// Character count
#include <iostream>
using namespace std;

string add(string s){
    string ans = "";
    int arr[10] = {0};
    for (char c = '0'; c<='9'; c++){
        int count=0;
        for (int j=0; j<s.length(); j++){
            if (s[j]==c){
                count++;
            }
        }
        arr[c-'0'] = count;
    }
   
    for (int i=0; i<10; i++){
        if (arr[i]!=0){
            char c = i + '0';
            ans += c;
            char d = arr[i] + '0';
            ans += d;
        }
    }
    
    return ans;
}

int main()
{
   string s;
   cin>>s;
   cout<<add(s);
   return 0;
}
