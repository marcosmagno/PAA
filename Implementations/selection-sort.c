#include <math.h> 
#include <stdio.h> 
// Esta função rearranja o vetor v[0..n-1]
// em ordem crescente.

void selecao (int n, int v[]) {
   for (int i = 0; i < n-1; ++i) {
      int min = i;
      for (int j = i+1; j < n; ++j) {
         if (v[j] < v[min]){
            min = j;
            }
         }
    int aux = v[i];
    v[i] = v[min];
    v[min] = aux;
   }
}

void printArray(int arr[], int n) { 
    int i; 
    for (i = 0; i < n; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
} 


int main() {
    int arr[] = {12, 11, 13, 5, 6, 20, 2, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    selecao(n, arr);
    printArray(arr, n);
}