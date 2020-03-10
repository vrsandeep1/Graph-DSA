def dfs(G,visited,startVertex):
	startVertex = int(startVertex)
	visited[startVertex] = True
	print(startVertex)
	for i in G[startVertex]:
		if(visited[i]==False):
			dfs(G,visited,i)

def printGraph(G):
	print("The graph represented in adjacency list form is as follows")
	for i in range(len(G)):
		for j in range(len(G[i])):
			print(G[i][j],end=" ")
		print()
def main():
	G=[]
	file = open('input.txt','r')
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
	visited=[False]*len(G)
	dfs(G,visited,0)

if(__name__=='__main__'):
	main()