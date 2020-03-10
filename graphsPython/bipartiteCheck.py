def doBipartiteCheck(G,startVertex):
	visited = [False]*len(G)
	level = [-1]*len(G)
	queue = []
	queue.append(startVertex)
	visited[startVertex] = True
	level[startVertex] = 0
	while(len(queue)!=0):
		print(queue)
		pop = queue.pop(0)
		for i in G[pop]:
			if(visited[i]==False):
				queue.append(i)
				visited[i]=True
				level[i] = level[pop] + 1
			elif(visited[i]==True and level[i] == level[pop]):
				return False
	return True
	

def printGraph(G):
	for i in range(len(G)):
		for j in range(len(G[i])):
			print(G[i][j],end=" ")
		print()
def main():
	G= [] 
	file = open('inputBp.txt','r')
	for line in file:
		line = line.strip()
		adjList = []
		first = True
		for node in line.split(" "):
			if(first==True):
				first = False
				continue
			adjList.append(int(node))
		G.append(adjList)
	#printGraph(G)
	if(doBipartiteCheck(G,0)):
		print("Graph is bipartite")
	else:
		print("Graph is not bipartite")
	
if(__name__=='__main__'):
	main()