import networkx as nx
import matplotlib.pyplot as plt
from networkx import all_shortest_paths

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split(','))

G = nx.Graph()

for i in range(n):
    G.add_node(i)

f = open("input.txt", "r")
# skip the first line
f.readline()
for i in range(m):
    line = f.readline().split(',')
    src_node = (line[0])
    dest_node = (line[1])
    weight = int(line[2])
    G.add_edge(src_node, dest_node, weight=weight)

f.close()

shortest_paths = all_shortest_paths(G, src_node, dest_node, weight=None, method='dijkstra')

shortest_paths = list(shortest_paths)
G.remove_nodes_from(list(nx.isolates(G)))

nodes = list(G.nodes())
# create a map of sources
for q in range(len(nodes)):
    print("Forwarding table for the node " + str(nodes[q]))
    # initialize all the variables
    min_weight = 0
    min_weight_node = nodes[0]
    current_path_weight = 0
    source = nodes[q]
    str_source = str(source)
    index = nodes.index(source)
    source_array = list(str_source)
    map_of_sources = {}
    map = {}
    # insert all the nodes with weight infinity except the source
    for i in range(len(nodes)):
        if (nodes[i] == source):
            continue
        map[nodes[i]] = float('inf')
    for i in range(len(nodes)):
        if (len(map) == 0):
            break
        # create a map containing each node and the weight of the shortest path to it
        # initialize the map
        # loop over the nodes
        if (i != 0):
            # concatenate the old source with the new source
            source = min_weight_node
            # get the index of the new source
            index = nodes.index(source)
            str_source = str_source + str(source)
            if min_weight_node in map:
                map.pop(min_weight_node)
                map_of_sources.pop(min_weight_node)
        if (i == 0):
            min_weight = 0
            min_weight_node = nodes[0]
            current_path_weight = 0
            source = nodes[q]
            str_source = str(source)
            index = nodes.index(source)
            source_array = list(str_source)
        print("step " + str(i) + ": ")
        print("Path: " + str_source)

        # loop over the neighbors of the current source
        for j in G.neighbors(source):
            # check if the neighbor is visited before
            if (str(j) in str_source):
                continue
            # variable the neighbor having the less weight to it
            min_weight = G[nodes[index]][j]['weight']
            min_weight_node = j
            if (min_weight < G[nodes[index]][j]['weight']):
                min_weight = G[nodes[index]][j]['weight']
                min_weight_node = j
            # loop over the source array and check if the node in source_array has a shorter path to the neighbor
            if (len(source_array) >= 1):
                for k in range(len(source_array)):
                    if (G.has_edge(source_array[k], j) == False):
                        continue
                    # check if there is a path from the node in source_array to the neighbor
                    if (G[source_array[k]][j]['weight'] == 0):
                        continue
                    # check if the path from the node in source_array to the neighbor is shorter than the current
                    # make sure that the key exists in the graph

                    if (G[source_array[k]][j]['weight'] < min_weight):
                        # print the neighbor and the weight of shortest path to it

                        print("neighbor: " + str(j) + " weight: " + str(
                            G[source_array[k]][j]['weight'] + current_path_weight))
                        min_weight = G[source_array[k]][j]['weight']
                        min_weight_node = j

            if (j in map):
                if (map[j] < min_weight + current_path_weight):
                    continue
                # add a couple of the neighbor and the corresponding source to the map with the weight of the shortest path to it
            map[j] = min_weight + current_path_weight
            map_of_sources[j] = source
            # insert the corresponding source to the map
            min_weight_node = min(map, key=map.get)
            min_weight = map[min_weight_node]

        # printing the map
        print("Nodes with corresponding weight: " + str(map))
        # print(map)
        print("Nodes with corresponding source: " + str(map_of_sources))
        # print(map_of_sources)
        # print the neighbor and the weight of shortest path to it
        # print("neighbor: " + str(min_weight_node) + " weight: " + str(min_weight+current_path_weight))
        # print("min weight: ")
        # print(min_weight+current_path_weight)
        # print("min weight node: ")
        # print(min_weight_node)
        source = min_weight_node
        # print ("source: ")
        # print(str_source)
        source_array = list(str_source)
        print("\n")
        current_path_weight = current_path_weight + min_weight
    print("**************************************************************************************************** ")
    print("\n")
    print("\n")
