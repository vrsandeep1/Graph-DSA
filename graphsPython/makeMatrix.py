


def main():
	
	G=[]
	file = open("input.txt","r")
	n=0
	for line in file:
		n = n+1
	file = open("input.txt","r")
	for line in file:
		line = line.strip()
		first = True
		adjacencyMatrix = [0]*n
		for node in line.split(" "):
			if(first==True):
				first = False
				continue
		
			adjacencyMatrix[int(node)] = 1
		
		G.append(adjacencyMatrix)
	print(G)

	
				

if(__name__=='__main__'):
	main()