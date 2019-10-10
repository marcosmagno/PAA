#include <iostream> 
#include <utility> 
#include <iostream> 
#include <vector> 
using namespace std; 

const int INF = 1000 * 1000 * 1000;
 




class MinCutStoerWagner {
public:
	pair<int, vector<int> > min_cut(vector<vector<int> > &g) 	{
		pair<int, vector<int> > res(INF, vector<int>());//res.first is total weight of deleted edges
								//res.second is vertices from one of components(sorted);
		int n = g.size();
		vector<vector<int> > v(n);
		for (int i = 0; i < n; ++i)
			v[i].assign (1, i);
 
		vector<int> w(n);
		vector<bool> exist(n, true), in_a(n);
		for (int ph = 0; ph < n-1; ph++) 
		{
			fill(in_a.begin(), in_a.end(), false);
			fill(w.begin(), w.end(), 0);
			for (int it = 0, prev; it < n-ph; it++) {
				int sel = -1;
				for (int i = 0; i < n; ++i)
					if (exist[i] && !in_a[i] && (sel == -1 || w[i] > w[sel]))
						sel = i;
				if (it == n - ph-1) {
					if (w[sel] < res.first)
					{
						res.first = w[sel];
						res.second = v[sel];
					}
					v[prev].insert(v[prev].end(), v[sel].begin(), v[sel].end());
					for (int i=0; i<n; ++i)
						g[prev][i] = g[i][prev] += g[sel][i];
					exist[sel] = false;
				}
				else {
					in_a[sel] = true;
					for (int i=0; i<n; ++i)
						w[i] += g[sel][i];
					prev = sel;
				}
			}
		}
 
		return res;		
	}
};

class Graph {
  public:
    int requiredCost(vector <string> roads) 
    {
		int n = roads.size();
		vector<vector<int> > g(n, vector<int> (n));
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				g[i][j] = roads[i][j] - '0';
 
		MinCutStoerWagner obj;
                //MinCutMaxFlow obj;  if you use MaxFlow algorithm
		return obj.min_cut(g).first;
    }
};


int main() {
    Graph graph;
	return 1;
}