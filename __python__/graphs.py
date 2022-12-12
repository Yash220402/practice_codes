edges = [[1,2],[5,1],[1,3],[1,4]]
vertices = []
for i in edges:
	for j in i:
		if j not in vertices: vertices.append(j)

graph = dict()

for vertex in vertices:
	graph[vertex] = []

for edge in edges:
	v1 = edge[0]
	v2 = edge[1]
	graph[v1].append(v2)
	graph[v2].append(v1)

v = [len(i) for i in list(graph.values())]
print(list(graph.keys())[v.index(max(v))])