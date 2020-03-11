class node:
	def __init__(self,value):
		self.rank = 0
		self.parent = self
		self.value = value
	def __str__(self):
		return str(self.value)
class DisjointSets:
	def makeset(self,value):
		return node(value)
	def union(self,node1,node2):
		while(node1.parent!=node1):
			node1 = node1.parent
		while(node2.parent!=node2):
			node2 = node2.parent


		if(node1.rank > node2.rank):
			node2.parent = node1
		elif(node2.rank > node1.rank):
			node1.parent = node2
		elif(node1.rank == node2.rank):
			node1.parent = node2
			node2.rank+=1
	def findset(self,node1):
		par = node1
		while(par.parent!=par):
			par = par.parent

		while(node1.parent != node1):
			tempNode = node1.parent
			node1.parent = par
			node1 = tempNode

		return node1
def main():
	ds = DisjointSets()
	nodes = []
	for i in range(10):
		nodes.append(ds.makeset(i))
	print(nodes[0].value)
	ds.union(nodes[0],nodes[1])
	print(ds.findset(nodes[0]).value)
	ds.union(nodes[0],nodes[2])
	print(ds.findset(nodes[2]).value)
	ds.union(nodes[0],nodes[5])
	print(ds.findset(nodes[5]))
if(__name__ == '__main__'):
	main()