#include <iostream>
#include <fstream>
#include <vector>
 
using namespace std;
 
int main() {
    const int N = 163;
    vector<bool>simple(N, true);
    ofstream f("simple.txt");
    for(int i = 2; i * i <= N; ++i) {
        if(simple[i] == true) {
            for(int j = i * i; j < N; j += i) {
                //cout << j << " ";
                simple[j] = false;
            }
        }
    }
 
    for(int i = 2; i < N; ++i) {
        if(simple[i] == true) {
            f << i << endl;
        }
    }
 
 
 
    cout << "Completed!";
}