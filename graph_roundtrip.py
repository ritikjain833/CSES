from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**6)
cycle_start=-1
cycle_end=0
def dfs(src,par):
	global cycle_end,cycle_start
	visited[src]=True
	for out in graph[src]:
		#print(src,out)
		if out==par:
			continue
		if visited[out]==True:
			cycle_end=src		
			cycle_start=out
			#print(cycle_start,cycle_end)
			return True	
		parent[out]=src
		
		if dfs(out,parent[out]):
			return True
	return False							

if __name__ == "__main__":
	n,m=map(int,input().split())
	graph=defaultdict(list)
	for _ in range(m):
		i,j=map(int,input().split())
		graph[i].append(j)
		graph[j].append(i)
	visited=[False]*(n+1)
	parent=[-1]*(n+1)
	for i in range(1,n+1):
		if visited[i]==False and dfs(i,parent[i]):
			break	
	if cycle_start==-1:
		print("IMPOSSIBLE")
	else:
		cycle=[]
		cycle.append(cycle_start)
		v=cycle_end
		while v!=cycle_start:
			cycle.append(v)
			#print(v)
			v=parent[v]
		cycle.append(cycle_start)	
		print(len(cycle))
		print(*cycle[::-1])




