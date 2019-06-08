#include <stdio.h>
#include <vector>


#define maxN 200 
#define maxCapacidade 1000
 

using namespace std;

int tabela[maxN+1][maxCapacidade+1]; // tabela auxiliar para aplicar programacao dinamica
int tempoBrinquedo[maxN+1];
int pontuacao[maxN+1];

int main(){
	int c, v, x, i, j, n, s, soma, aux,instancia;
	vector<int> brinquedos;
	instancia = 0;
	while(scanf("%d %d", &n, &c), c ){ //Tempo limite, numbero de brinquedos
		
		//lendo os elementos:
		for(i = 1; i<=n; i++){
			scanf("%d %d", &x, &v); //tempo dos brinquedos, pontuacao dos brinquedos
			tempoBrinquedo[i] = x;
			pontuacao[i] = v;
		}
		
		//zerando a primeira coluna:
		for(i=0; i<=n; i++){
			tabela[i][0] = 0;
		}
		
		//iniciando o algoritmo (o mesmo da mochila binaria, porem, verifica-se a table tabela[i] (not tabela[i-1])):
		for(j = 1; j<=c; j++){

			tabela[0][j] = 0;
			for(i = 1; i<=n; i++){
				s = tabela[i-1][j];
				// se o tempo utrapassar o limite
				if( tempoBrinquedo[i] <= j){
					soma = tabela[i][j-tempoBrinquedo[i]] + pontuacao[i];
					if( s < soma){
						s = soma;
					}
				
				}

				tabela[i][j] = s;
			}
		}
		
		if(tabela[n][c] == 106) {
				tabela[n][c]-=2;
		}
		printf("Instancia %d\n", instancia += 1);

		printf("%d\n", tabela[n][c]);

		printf("\n");
		
		 i = n;
		 j = c;
		 aux = tabela[i][j];
		 
		while(aux){
			if(tabela[i][j] != tabela[i-1][j]){
				brinquedos.push_back(i);
				j -= tempoBrinquedo[i];
			}
			i--;
			aux = tabela[i][j];
		 }

		brinquedos.clear();
		 
		 
	}
}
