#include <iostream>
using namespace std;
#define max(a,b) (((a)>(b))?(a):(b));


int Max_Subarray_Sum(int arr[], int n) {

    if(n == 1) {
        if(arr[0] < 1){
            return 0;
        }
        else {
        return arr[0];
        exit(0);
        }
        
    }
    if(n == 0) {
        return 0;
        exit(0);
    }

    int m = n/2;
    int left_MSS = Max_Subarray_Sum(arr, m);
    int right_MSS = Max_Subarray_Sum(arr+m, n-m);
    int leftsum = 0;
    int rightsum = 0;
    int sum = 0;
    
    for(int i = m; i<n; i++) {
        sum += arr[i];
        rightsum = max(rightsum, sum);
    }

    sum = 0;
    for(int i = (m-1); i >=0; i--) {
        sum += arr[i];
        leftsum = max(leftsum, sum);
    }

    int ans = max(left_MSS, right_MSS);
    
    return max(ans,leftsum + rightsum);
}

int main() {
int arr[50];
int result[50];
int dias, custoPorDia;
int receitas;
    while(cin >> dias >> custoPorDia) {
    for(int i = 0; i < dias; i++) {
        scanf("%d", &receitas);
        arr[i] = receitas;
        result[i] = arr[i] - custoPorDia;
    }
    printf("%d\n", Max_Subarray_Sum(result, dias));

}

}
