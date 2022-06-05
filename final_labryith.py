import sys
from collections import deque
rows,cols=[int(s) for s in sys.stdin.readline().split()]
grid=[[0]*cols for _ in range(rows)]
src,dest=None,None
for r in range(rows):
	for c,ch in enumerate(sys.stdin.readline().strip()):
		if ch=="A":
			src=(r,c)
		elif ch=="B":
			dest=(r,c)
		grid[r][c]=ch
directions=[[-1,0],[0,1],[1,0],[0,-1]]
def bfs(grid,src,dest):
	queue=deque()
	queue.append(src)
	parents=[[None]*(len(grid[0])) for _ in range(len(grid))]
	parents[src[0]][src[1]]=-1
	while queue:
		node=queue.popleft()
		if node==dest:
			print("YES")
			path=[]
			while parents[node[0]][node[1]]!=-1:
				prev=parents[node[0]][node[1]]
				if prev[0]-node[0]>0:
					path.append("U")
				if prev[0]-node[0]<0:
					path.append("D")
				if prev[1]-node[1]>0:
					path.append("L")
				if prev[1]-node[1]<0:
					path.append("R")
				node=prev
			print(len(path))
			print("".join((s for s in reversed(path))))
			return
		for dr,dc in directions:
			nr=dr+node[0]
			nc=dc+node[1]
			if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc]!='#' and parents[nr][nc] is None:
				parents[nr][nc]=node
				queue.append((nr,nc))
	print("NO")	
bfs(grid,src,dest)									
