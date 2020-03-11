import disjointsets
import operator

def runKruskal(G,linecount):
	ds = disjointsets.DisjointSets()
	nodes = []
	for i in range(linecount):
		nodes.append(ds.makeset(i))
	allEdge = []

	for pair in G:
		if(ds.findset(nodes[pair[0]]) != ds.findset(nodes[pair[1]])):
			ds.union(nodes[pair[0]],nodes[pair[1]])
			allEdge.append(pair)
	print(allEdge)

def main():
	G = []
	linecount = 0
	file = open('kruskal_input_2.txt','r')
	for line in file:
		line = line.strip()
		firstVal = 0
		first = True
		linecount+=1
		for node1 in line.split(" "):
			if(first):
				firstVal = int(node1)
				first = False
				continue
			node,weight = node1.split(",")
			G.append([firstVal,int(node),int(weight)])
	#print(G)

	G.sort(key = operator.itemgetter(2))

	#print(G)

	runKruskal(G,linecount)
	

if(__name__ == '__main__'):
	main()