from collections import defaultdict
from enum import Enum
import pandas as pd


graph = defaultdict(list)

def addEdge(graph,u,v):
	graph[u].append(v)


def generate_edges(graph):
	edges = []

	for node in graph:
		for neighbour in graph[node]:
			edges.append((node, neighbour))
	return edges


def generate_graph():
	print("Easy going : 1 " + "\n" + "High standards : 2" + "\n" + "Enjoy alone time : 3" + "\n" + "Dislike confrontation : 4" + "\n" + "Prefer crowds : 5" + "\n" + "Like concerts : 6" + "\n" + "Explore different cuisines : 7" + "\n" + "Do homework : 8" + "\n" + "Explore places : 9 ")
	inp = int(input("Chose your Input : "))
	print(inp)
	data = pd.read_excel(r'data.xlsx')
	name = data.iloc[:,0]
	val = data.iloc[:,inp]
	for i in range(0,name.__len__()):
		addEdge(graph,name[i],val[i])



# declaration of graph as dictionary
generate_graph()
print(generate_edges(graph))
exec(open("Cluster.py").read())
exec(open("ClosestPair.py").read())

