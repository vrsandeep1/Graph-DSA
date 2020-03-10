from queue import Queue
def doBFS(G):
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
		for node in line.split(' '):
			if(first):
				first = False
				continue
			adjacentVertices.append(int(node))
		G.append(adjacentVertices)

	#printGraph(G)
	if(input("Do you want to do BFS?")=="YES"):
		doBFS(G)

if ( __name__ == "__main__"):
	main()
