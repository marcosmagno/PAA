#include <iostream>
using namespace std;
#define max(a,b) (((a)>(b))?(a):(b));


//int SixFlags(int arr[], int n) {
    
//    return max(ans,leftsum + rightsum);
//}

int main() {
int arr[50];
int result[50];
int duracao, pontuacao, atracoes;

while (scanf("%d %d", &atracoes, &duracao) != EOF){
        printf("atracao duracao %d %d\n", atracoes, duracao);
        for(int i = 0; i < atracoes; i++) {
            scanf("%d %d", &duracao, &pontuacao);
            printf("linha %d %d\n", duracao, pontuacao);
        }
              
}


}
