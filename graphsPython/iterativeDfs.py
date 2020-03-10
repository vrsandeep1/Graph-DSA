

def iterativeDfs(G,startVertex):
	visited = [False]*len(G)
	stack = []
	stack.append(startVertex)
	visited[startVertex] = True
	while(len(stack)!=0):

		print(stack)
		poppedEle = stack.pop(0)
		print(poppedEle,end = " ")
		for i in G[poppedEle]:
			if(visited[i]==False):
				visited[i] = True
				stack.insert(0,i)


def printGraph(G):
	for i in range(len(G)):
		for j in range(len(G[i])):
			print(G[i][j],end=" ")
		print()
def main():
	G = []
	file = open('input.txt','r')
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
	iterativeDfs(G,0)
	#printGraph(G)
if(__name__=='__main__'):
	main()