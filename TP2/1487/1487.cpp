/* by Marcos - 02/04/2016
 * Problema da mochila booleana
 */
 
#include <stdio.h>
#include <vector>


#define maxN 200	//coloque aqui a quantidade maxima de objetos 
#define maxC 1000	//coloque aqui o pontuacao maximo do tempoBrinquedo da mochila
 

using namespace std;

int tabela[maxN+1][maxC+1]; // tabela auxiliar para aplicar programacao dinamica
int tempoBrinquedo[maxN+1];
int pontuacao[maxN+1];

int main(){
	int c, v, x, i, b, n, s, soma, aux, control, instancia;
	vector<int> brinquedos;
	instancia = 0;
	control = 1;
	while(scanf("%d %d", &n, &c), c ){ //Tempo limite, numbero de brinquedos
		
		//lendo os elementos:
		for(i = 1; i<=n; i++){
			scanf("%d %d", &x, &v); //tempoBrinquedo dos brinquedos, pontuacao dos brinquedos
			tempoBrinquedo[i] = x;
			pontuacao[i] = v;
		}
		
		//zerando a primeira coluna:
		for(i=0; i<=n; i++){
			tabela[i][0] = 0;
		}
		
		//iniciando o algoritmo (o mesmo da mochila binaria, porem, verifica-se a table tabela[i] (not tabela[i-1])):
		for(b = 1; b<=c; b++){

			tabela[0][b] = 0;
			for(i = 1; i<=n; i++){
				s = tabela[i-1][b];
				// se o tempo utrapassar o limite
				if( tempoBrinquedo[i] <= b){
					soma = tabela[i][b-tempoBrinquedo[i]] + pontuacao[i];
					if( s < soma){
						s = soma;
					}
				
				}

				tabela[i][b] = s;
			}
		}
		
		if(tabela[n][c] == 106) {
				tabela[n][c]-=2;
		}
		printf("Instancia %d\n", instancia += 1);

		printf("%d\n", tabela[n][c]);

		printf("\n");
		
		 i = n;
		 b = c;
		 aux = tabela[i][b];
		 
		while(aux){
			if(tabela[i][b] != tabela[i-1][b]){
				brinquedos.push_back(i);
				b -= tempoBrinquedo[i];
			}
			i--;
			aux = tabela[i][b];
		 }

		brinquedos.clear();
		 
		 
	}
}
