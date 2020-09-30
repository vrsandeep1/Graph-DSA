def detectCycle(G,visited,parent,startVertex,parentIndex):
	visited[startVertex] = True
	parent[startVertex] = parentIndex
	for i in G[startVertex]:
		if(visited[i]==False):
			detectCycle(G,visited,parent,i,startVertex)
		elif(visited[i]==True and parent[startVertex]!=i):
			print("Cycle exists")
			exit(0)
	
	# exit(0)
def main():
	G = []
	file = open('cycle.txt','r')
	for line in file:
		line = line.strip()
		adjList = []
		first = True
		for node in line.split(" "):
			if(first == True):
				first = False
				continue
			adjList.append(int(node))
		G.append(adjList)
	visited = [False]*len(G)
	parent = [-1]*len(G)
	for v in range(0,len(G)):
		if visited[v]==False:
			detectCycle(G,visited,parent,v,-1)

	 
	print("Cycle does not exist")
	

if(__name__=='__main__'):
	main()