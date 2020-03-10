time = 0
def topologicalSort(G,topSort,visited,startVertex):
	global time
	visited[startVertex] = True
	time = time + 1

	for adjVertex in G[startVertex]:
		if(not visited[adjVertex]):
			topologicalSort(G,topSort,visited,adjVertex)

	time = time + 1
	topSort.append(startVertex)
def findLongestPath(topSort,indegree,G,longestPath):

	while(len(topSort)!=0):
		vertex = topSort.pop()
		for adj in G[vertex]:
			if(indegree[vertex]==0):
				longestPath[adj] = 1
			else:
				longestPath[adj] = max(longestPath[adj],longestPath[vertex] + 1)

	print(longestPath)
def main():
	G = []
	file = open('longest_path_topological_sort_input.txt','r')
	for line in file:
		line = line.strip()
		adjacentVertices = []
		first = True
		for node in line.split(" "):
			if(first):
				first = False
				continue
			adjacentVertices.append(int(node))
		G.append(adjacentVertices)
	#print(G)
	topSort = []
	visited = [False]*len(G)
	indegree = [0]*len(G)
	longestPath = [0]*len(G)
	for i in range(len(G)):
		for j in G[i]:
			indegree[j] = indegree[j] + 1
	for i in range(len(G)):
		if(not visited[i]):
			topologicalSort(G,topSort,visited,i)

	#print(topSort)

	findLongestPath(topSort,indegree,G,longestPath)
if(__name__ == "__main__"):
	main()