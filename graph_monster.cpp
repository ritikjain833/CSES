#include<bits/stdc++.h>
using namespace std;

int dx[]={-1,1,0,0};
int dy[]={0,0,1,-1};
char go[]={'U','D','R','L'};
char A[1000][1000];
int nex[1005][1005];
int main(){

	int n,m;
	cin>>n>>m;
	int x,y;
	queue<pair<int,int>> q;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> A[i][j];
			if (A[i][j] == 'M') {
				q.push({i,j});
				
			} else if (A[i][j] == 'A') {
				x=i;
				y=j;
			}
		}
	}
	q.push({x,y});
	nex[x][y]=-1;
	while (!q.empty()){
		pair<int,int> t=q.front();
		q.pop();

		int x,y;
		x=t.first;
		y=t.second;
		if (A[x][y]=='A' &&(x==0||x==n-1|| y==0||y==m-1))
		{
			cout<<"YES"<<endl;
			string ans;
			int d=nex[x][y];
			while (d!=-1){
				ans+=go[d];
				x-=dx[d];
				y-=dy[d];
				d=nex[x][y];

			}
			reverse(ans.begin(),ans.end());
			cout<<ans.size()<<endl;
			cout<<ans;
			return 0;
		}
		for (int i=0;i<4;i++){
			int xx=t.first+dx[i];
			int yy=t.second+dy[i];
			if (xx>=0 && xx<n && yy>=0 && yy<m && A[xx][yy]=='.'){
				A[xx][yy]=A[t.first][t.second];
				if (A[xx][yy]=='A'){
					nex[xx][yy]=i;
				}
				q.push({xx,yy});
			}

		}

	}
	cout<<"NO"<<endl;

}