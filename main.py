#importing lib
from algo_src.utils import nested_dict, get_sorted, aggregate_ranks
from algo_src.graph import Graph
from algo_src.hits_algorithm import hits

#reading data
filename = "SBCN-BCTM.txt"

data = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        edge = line.split(',')
        edge[2] = float(edge[2])
        data.append(edge)

#create weighted map
mapper = nested_dict(2, float)

for edge in data:
    mapper[edge[0]][edge[1]] = edge[2]

#creating the graph
g = Graph()

edge_limit = 20000
rank_limit = 10

for i,edge in enumerate(data):

    if(i%1000 == 0):
        print("Added {} edges".format(i))

    if i == edge_limit:
        break

    parent = edge[0]
    child = edge[1]
    g.add_edge(parent, child)

g.sort_nodes()

#applying hits algorithm
hits(graph=g, iteration=20, weights=mapper)

#display hub and auth values
#g.display_hub_auth_values()

hub = g.get_hub_list()
auth = g.get_auth_list()
node = g.get_node_list()

#ranking based on hub
sorted_hub = get_sorted(node, hub)

print("-----Ranking based on hub values-----")
for i in range(rank_limit):
    print(sorted_hub[i])

#ranking based on auth
sorted_auth = get_sorted(node, auth)

print("-----Ranking based on auth values-----")
for i in range(rank_limit):
    print(sorted_auth[i])

#aggregated ranking
node_ranking = aggregate_ranks([sorted_hub, sorted_auth], 2)  

print("-----Final Ranking-----")
for i in range(rank_limit):
    print(node_ranking[i])

        