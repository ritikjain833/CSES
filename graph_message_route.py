from collections import defaultdict,deque
def bfs(graph,src,n):
	queue=deque()
	queue.append((1,1))
	visited[1]=True
	while queue:
		aux,dist=queue.popleft()
		#print(aux,dist)
		for v in graph[aux]:
			if visited[v]==False:
				parent[v]=aux
				queue.append((v,dist+1))
				visited[v]=True
			#print(v)	
			if v==n:
				#print(v,dist)
				return dist+1

	return -1				


if __name__ == "__main__":

	n,m=map(int,input().split())
	graph=defaultdict(list)
	for _ in range(m):
		i,j=map(int,input().split())
		graph[i].append(j)
		graph[j].append(i)
	visited=[False]*(n+1)
	#print(graph)
	
	parent=[0]*(n+1)
	parent[1]=1
	dist=bfs(graph,1,n)
	src=1
	if dist!=-1:
		print(dist)
		dest=n
		ans=[]
		ans.append(dest)
		while dest!=src:
			temp=parent[dest]
			ans.append(temp)
			dest=temp
		print(*ans[::-1])
	else:
		print("IMPOSSIBLE")	


