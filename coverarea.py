import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def graphgen(N,xmin,xmax,ymin,ymax):
	G = nx.Graph()

	verts = []
	for i in range(N):
		x = np.random.uniform(xmin,xmax)
		y = np.random.uniform(ymin,ymax)

		verts.append([x,y])
		G.add_node(i,pos=(x,y))

		for j in range(len(verts)):
			if not j == i and isclose([x,y],verts[j],1):
				G.add_edge(j,i)

		# fig = plt.figure(figsize=(10,10))
		# plt.xlim([-5.5,5.5])
		# plt.ylim([-5.5,5.5])
		# plt.scatter(np.array(verts)[:,0],np.array(verts)[:,1])
		# plt.savefig('t={}'.format(i))
		# plt.close(fig)
		# print(verts)

	pos=nx.get_node_attributes(G,'pos')

	fig, ax = plt.subplots(figsize=(9,9))
	nx.draw(G,pos,node_size=10,ax=ax)
	limits=plt.axis('on')
	ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
	plt.show()

	# print(len(G.nodes))
	# return verts

def isclose(u,v,delta):
	return d(u,v) <= delta

def count_neighbor(verts,u,delta):
	count = 0
	for i in range(len(verts)):
		if d(u,verts[i]) < delta:
			count += 1

	return count

def d(u,v):
	return np.sqrt((v[0]-u[0])**2+(v[1]-u[1])**2)

graphgen(100,-5,5,-5,5)
