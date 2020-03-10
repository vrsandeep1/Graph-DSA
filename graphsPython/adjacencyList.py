from collections import defaultdict
from queue import Queue
class Graph:
	def __init__(self):
		self.listAdj = defaultdict(list)

	def addEdge(self,u,v):
		self.listAdj[u].append(v)
		self.listAdj[v].append(u)
	def printGraph(self):
		for i in range(len(self.listAdj)):
			for j in range(len(self.listAdj[i])):
				print(self.listAdj[i][j],end="")

	def doBFS(self):
		G= self.listAdj
		visited = [False]*len(G)
		queue = Queue()
		queue.put(0)
		visited[0] = True
		while(queue.empty()==False):
			pop = queue.get()
			print(pop,end="  ")
			for j in G[pop]:
				if(visited[j]==False):
					visited[j] = True
					queue.put(j)
	
if (__name__=='__main__'):
	g = Graph()
	g.addEdge(0, 1) 
	g.addEdge(0, 2) 
	g.addEdge(1, 2) 
	g.addEdge(2, 0) 
	g.addEdge(2, 3) 
	g.addEdge(3, 3)
	#g.printGraph()
	g.doBFS()