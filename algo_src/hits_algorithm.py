def hits(graph, iteration, weights):
    for i in range(iteration):
        print("HITS Algorithm - Iteration - {}".format(i+1))
        hits_per_iteration(graph, weights)

def hits_per_iteration(graph, weights):
    for node in graph.nodes:
        node.update_hub_value(weights)
        node.update_auth_value(weights)
    graph.normalization()
