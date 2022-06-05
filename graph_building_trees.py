from collections import defaultdict,deque
import sys
def bfs(src):
	visited[src]=True
	color[src]=1
	queue=deque()
	queue.append((src,1))
	#flag=True
	while queue:
		aux,temp=queue.popleft()
		for out in graph[aux]:
			if color[out]==0:
				visited[out]=True
				if (temp+1)%2==0:
					color[out]=2
					queue.append((out,0))	
				else:
					color[out]=1	
					queue.append((out,1))
			elif color[out]==temp:
				return -1
	return 0			



if __name__ == "__main__":

	n,m=map(int,input().split())
	graph=defaultdict(list)
	for _ in range(m):
		i,j=map(int,input().split())
		graph[i].append(j)
		graph[j].append(i)
	visited=[False]*(n+1)
	color=[0]*(n+1)
	flag=True
	for i in range(1,n+1):
		if visited[i]==False:
			x=bfs(i)
			if x==0:
				continue
			elif x==-1:
				flag=False
				break
	if flag==True:			
		print(*color[1:])
	else:
		print("IMPOSSIBLE")			
			