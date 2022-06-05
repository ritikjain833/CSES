from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**6)
def bfs(r,c):
	queue=deque()
	res=""
	queue.append((r,c,0,res))
	while queue:
		r,c,dist,res=queue.popleft()
		for dr,dc,path in directions:
			nr=dr+r
			nc=dc+c
			
			if nr>=0 and nr<n and nc>=0 and nc<m and visited[nr][nc]==False:
				queue.append((nr,nc,dist+1,res+path))
				visited[nr][nc]=True
			if matrix[nr][nc]=="B":
				return dist+1,queue.pop()[3]
				
						
	

if __name__ == "__main__":

	n,m=map(int,input().split())
	matrix=[[0]*(m) for _ in range(n)]
	for i in range(n):
		a=input()	
		for j in range(len(a)):
			matrix[i][j]=a[j]
	visited=[[False]*(m) for _ in range(n)]
	#print(matrix)
	directions=[[-1,0,"U"],[1,0,"D"],[0,1,"R"],[0,-1,"L"]]
	count=0
	res=""
	for i in range(n):
		for j in range(m):
			if matrix[i][j]=="#":
				visited[i][j]=True

	for i in range(n):
		for j in range(m):
			if matrix[i][j]=="A":
				visited[i][j]=True
				count,res=bfs(i,j)
				#print(count)
				break

	if count>0:
		print("YES")
		print(count)
		print(res)
	else:
		print("NO")					