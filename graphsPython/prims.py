import heapq
import sys



def doPrims(G,pq,startVertex):
    visited = [False]*len(G)
    for adj,wt in G[startVertex]:
        pq.append([wt,startVertex,adj])
    heapq.heapify(pq)
    addEdge = []
    while(len(addEdge) < len(G) - 1):
        print(pq)
        wt,frm,to = heapq.heappop(pq)
        addEdge.append([wt,frm,to])
        visited[frm] = True

        for adjVert,adjWt in G[to]:
            if(not visited[adjVert]):
                heapq.heappush(pq,[adjWt,to,adjVert])

    print(addEdge)

def main():
    G = [] 

    file=open('prims_input_1.txt','r')
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

    doPrims(G,pq,0)

if __name__ == '__main__':
    main()