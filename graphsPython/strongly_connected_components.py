from collections import defaultdict

time = 0

def dfs(GR,visited,startTime,endTime,parent,startVertex,stack):
	global time
	visited[startVertex] = True
	startTime[startVertex] = time
	time = time + 1

	for adjVertex in GR[startVertex]:
		if(visited[adjVertex] == False):
			parent[adjVertex] = startVertex
			dfs(GR,visited,startTime,endTime,parent,adjVertex,stack)

	stack.append(startVertex)
	endTime[startVertex] = time
	time = time + 1	


def dfsP(G,visited,vertex,vertices):
	visited[vertex] = True
	vertices.append(vertex) 
	for i in G[vertex]:
		if(not visited[i]):
			dfsP(G,visited,i,vertices)

def reverseGraph(G,visited,startTime,endTime,parent):
	GR = defaultdict(list)
	
	stack = []
	for i in range(len(G)):
		for j in G[i]:
			GR[j].append(i)

	#print(GR)
	for i in range(len(G)):
		if(not visited[i]):
			dfs(GR,visited,startTime,endTime,parent,i,stack)
	#print(endTime)

	print(stack)
	newVisited = [False]*len(G)

	while(len(stack)!=0):
		vertex = stack.pop()
		if(newVisited[vertex]):
			continue
		vertices = []
		dfsP(G,newVisited,vertex,vertices)
		print(vertices)
	


def main():
	G = []
	file = open('input_strongly_connected_components2.txt','r')
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
	visited = [False]*len(G)
	startTime = [-1]*len(G)
	endTime = [-1]*len(G)
	parent = [-1]*len(G)

	reverseGraph(G,visited,startTime,endTime,parent)

	#SCC(G,visited,startTime,endTime,parent,0)	


if(__name__ == '__main__'):
	main()