// Calculating large factorial values
/* 
Limit of storing large value is:
	8 bytes = 64 bits (unsigned long long)
	-> this can hold a positive number in 
	   range 0 to 18,446,744,073,709,551,615.
*/

#include<iostream>
using namespace std;

class Factorial {

    public:

    void GetFactorial (int number) {

        int store[1000] = {0};
        int index = 0;
        int result = number;

        while (result >= 1) {
            store[index++] = result%10;
            result /= 10;
        }
        number--;

        int carry = 0;
        while (number > 0) {
            int i = 0;
            while (i < index) {
                result = store[i] * number + carry;
                store[i++] = result%10;
                carry = result/10;
            }
            while (carry > 0) {
                store[i++] = carry%10;
                carry /= 10;
            }
            number -= 1;
            index = i;
        }

        cout << "Factorial : ";
        for (int i=index-1; i>=0; i--) {
            cout << store[i];
        } cout << endl;
    }
};

int main() {

    Factorial f;
    int num;
    cout << "Enter number : ";
    cin >> num;
    f.GetFactorial(num);

    return 0;
}

