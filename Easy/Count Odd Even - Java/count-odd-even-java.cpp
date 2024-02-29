//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

void countOddEven(int a[], int n) {
    int c=0;
    int q=0;
    for(int i=0;i<n;i++){
        if(a[i]%2==0)
        c+=1;
        else
        q+=1;
        
    }
    cout<<q<<" "<<c;
}


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        countOddEven(a, n);
        cout << endl;
    }
}
// } Driver Code Ends