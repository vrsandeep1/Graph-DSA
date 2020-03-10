def twoEdgeConnected(G):
	
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
	twoEdgeConnected(G)
if(__name__=='__main__'):
	main()