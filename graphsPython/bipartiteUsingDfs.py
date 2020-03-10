def checkBipartite(G,visited,color,startVertex,parentIndex):
	visited[startVertex] = True
	color[startVertex] = not color[parentIndex]
	for i in G[startVertex]:
		if(visited[i]==False):
			checkBipartite(G,visited,color,i,startVertex)
		elif(visited[i]==True and color[i]==color[startVertex]):
			print("Not bipartite")
			exit(0)
	print("Bipartite")
	exit(0)
def main():
	G=[]
	file = open('cycle.txt','r')
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
	visited = [False]*len(G)
	color = [False]*len(G)
	checkBipartite(G,visited,color,0,0)
if(__name__=='__main__'):
	main()