import sys
import heapq

def doDijkstra(G,pq,startVertex,finalDistance,parent):
	
	finalDistance[startVertex] = 0
	pq.append([0,startVertex])
		
	while(len(pq)!=0):
		print(pq)
		dist,vert = heapq.heappop(pq)
		
		for adjVert,adjDist in G[vert]:
			if(finalDistance[adjVert] > finalDistance[vert] + adjDist):
				finalDistance[adjVert] = finalDistance[vert] + adjDist
				heapq.heappush(pq,[finalDistance[adjVert],adjVert])
				parent[adjVert] = vert
	print(finalDistance)
	print(parent)

def main():
	G = [] 

	file=open('inputdijkstra5.txt','r')
	for line in file:
		line=line.strip()
		adjacentVertices = []
		first=True
		for edge in line.split(' '):
			if first:
				first=False
				continue
			node,weight = edge.split(',')
			adjacentVertices.append((int(node),int(weight)))
		G.append(adjacentVertices)

	file.close()
	pq = []
	finalDistance = [sys.maxsize]*len(G)
	parent = [-1]*len(G)

	doDijkstra(G,pq,0,finalDistance,parent)

if __name__ == '__main__':
	main()