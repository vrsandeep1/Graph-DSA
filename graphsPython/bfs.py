def bfs(G,startVertex):
	visited = [False]*len(G)
	distance = [-1]*len(G)
	queue = []
	queue.append(startVertex)
	visited[startVertex] = True
	distance[startVertex] = 0
	while(len(queue)!=0):
		poppedEle  = queue.pop(0)
		print(poppedEle,distance[poppedEle])
		for i in G[poppedEle]:
			if(visited[i]==False):
				visited[i]=True
				queue.append(i)
				distance[i] = distance[poppedEle] + 1



def printGraph(G):
	for i in range(len(G)):
		for j in range(len(G[i])):
			print(G[i][j],end=" ")
		print()

def main():
	G=[]
	file = open('input.txt','r')
	for line in file:
		line = line.strip()
		adjacentVertices = []
		first = True
		for node in line.split(" "):
			if(first==True):
				first = False
				continue
			adjacentVertices.append(int(node))
		G.append(adjacentVertices)
	#printGraph(G)
	bfs(G,0)



if(__name__=='__main__'):
	main()