#include <bits/stdc++.h>

using namespace std;
    int tabela[100000+10][60];
    const  int MOD = 1e9+7;

int main(){
	int t,min,max, maxMin;
    int result =0 ;
	cin >> t >> min >> max;
    maxMin = max - min;
    memset(tabela, 1, sizeof(tabela));

    for(int i = 0; i < maxMin + 1; i++) {
        for(int j = 0; j < t ; j++) {
            tabela[i][0] = 1;
        }
        
    }
    
    for(int i = 1; i < t; i++) { // coluna
        for(int j = 0; j < maxMin + 1; j++ ){ // linha
            if(j == 0) {
                // borda superior
                tabela[j][i] = tabela[j+1][i-1];
            }else if(j == maxMin) {
                // borda inferior
                tabela[j][i] = tabela[j-1][i-1];
                
            } else {
                tabela[j][i] = (tabela[j-1][i-1] + tabela[j+1][i-1]) % MOD;

            } if(i == t-1) {
                result = (result + tabela[j][i]) % MOD;
            }
        }
    }
    cout << result << endl;

}
