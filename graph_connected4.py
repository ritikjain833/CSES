from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**6)
def dfs(src):
	visited[src]=True
	for out in graph[src]:
		if visited[out]==False:
			dfs(out)



if __name__ == "__main__":

	n,m=map(int,input().split())
	graph=defaultdict(list)
	for _ in range(m):
		i,j=map(int,input().split())
		graph[i].append(j)
		graph[j].append(i)
	visited=[False]*(n+1)
	aux=[]	
	count=0
	for i in range(1,n+1):
		if visited[i]==False:
			dfs(i)
			aux.append(i)
			count+=1
	print(count-1)
	ans=[]
	for i in range(len(aux)-1):
		ans.append([aux[i],aux[i+1]])
	
	for i,j in ans:
		print(i,j)


