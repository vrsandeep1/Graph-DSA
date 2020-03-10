def doBFS(startVertex,visited,G,count):
	visited[startVertex] = True
	queue = []
	queue.append(startVertex)
	while(len(queue)!=0):
		popped = queue.pop(0)
		print("cluster number "+str(count)+" vertex number is "+str(popped))
		for i in G[popped]:
			if(visited[i]==False):
				visited[i]=True
				queue.append(i)

def computeConnectedComponent(G):
	visited = [False]*len(G)
	count = 0
	for i in range(len(G)):
		if(visited[i]==False):	
			count = count + 1
			doBFS(i,visited,G,count)
	print("Total number of disconnected components in the graph is equal to " + str(count))

def printGraph(G):
	for i in range(len(G)):
		for j in range(len(G[i])):
			print(G[i][j],end=" ")
		print()
def main():
	G = []
	file = open('connectedComp2.txt','r')
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
	computeConnectedComponent(G)

if(__name__ == "__main__"):
	main()