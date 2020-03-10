time = 0
def isScc(G,visited,startTime,parent,endTime,startVertex):
	global time
	visited[startVertex] = True
	startTime[startVertex] = time
	tempTime = time
	time = time + 1

	for adjVertex in G[startVertex]:
		if(not visited[adjVertex]):
			tempTime = min(tempTime,isScc(G,visited,startTime,parent,endTime,adjVertex))
			parent[adjVertex] = startVertex
		elif(parent[adjVertex]!=startVertex):
			tempTime = min(tempTime,startTime[adjVertex])

	if(tempTime == startTime[startVertex] and startVertex!=0):
		print("Graph is not strongly Connected")
		exit()
	endTime[startVertex] = time
	time = time + 1
	return tempTime



def main():
	G = []
	file = open('inputNotStronglyConnect.txt','r')
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
	parent = [-1]*len(G)
	endTime = [-1]*len(G)
	isScc(G,visited,startTime,parent,endTime,0)
	print(startTime)
	print(endTime)
	print("Strongly connected graph")

main()