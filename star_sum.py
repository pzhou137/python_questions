from collections import defaultdict
import heapq
def best_sum_kstar(g_nodes: int, g_from: list[int], g_to: list[int], values: list[int], k: int) -> int:
    """
    Given a graph with nodes and edges, find the best sum of k stars.
    """
    # Create a dictionary to store the graph
    graph = defaultdict(list)
    for i in range(len(g_from)):
        graph[g_from[i]].append(g_to[i])
        graph[g_to[i]].append(g_from[i])
    
    max_sum = int('-inf') # initialize the max sum to negative infinity

    for node in range(g_nodes):
        connect_values = [values[neighbor] for neighbor in graph[node]] # get the values of the connected nodes

        # alternative way to get the values of the connected nodes
        # connect_values = []
        # for neighbor in graph[node]:
        #     connect_values.append(values[neighbor])



        potential_sum = values[node] # initialize the star sum to the value of the current node

        if connect_values and k > 0:
            best_values = heapq.nlargest(k, connect_values, key=lambda x: x) # get the k largest values from the connected nodes
            # potential_sum = star_sum + sum([x for x in best_values if x > 0]) # calculate the potential sum of the star sum and the k largest values
            for x in best_values:
                if x > 0:
                    potential_sum += x


        max_sum = max(max_sum, potential_sum) # update the max sum if the star sum is greater than the current max sum

    return max_sum








