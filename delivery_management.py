from collections import defaultdict, deque


def order(city_nodes: int, city_from: list[int], city_to: list[int], company: int) -> list[int]:
    """
    Determine the optimal order of deliveries for a company based on city connections.
    
    Args:
        city_nodes (int): The number of cities
        city_from (list[int], length = N): The list of cities where deliveries start
        city_to (list[int], length = N): The list of cities where deliveries end
        company (int): The company where the route starts
        
    Returns:
        list[int]: The optimal order of deliveries
    """

    #create a bidirectional graph
    graph = defaultdict(list)
    for i in range(city_nodes):
        # add the edge to the graph
        # city_from[i] is the source city
        # city_to[i] is the destination city
        # graph[city_from[i]] is the list of cities connected to city_from[i]
        # append the destination city to the list
        graph[city_from[i]].append(city_to[i])
        # add the reverse edge to the graph
        # graph[city_to[i]] is the list of cities connected to city_to[i]
        # append the source city to the list
        graph[city_to[i]].append(city_from[i])
    
    distances = [-1] * (city_nodes + 1) 
    # creates a list of -1s with the length of the number of cities + 1
    # +1 because we are using 1-based indexing
    # distances[0] is not used
    # distances[1] is the distance from the company to the first city
    # distances[2] is the distance from the company to the second city
    # ...
    # distances[city_nodes] is the distance from the company to the last city

    distances[company] = 0
    # set the distance from the company to itself to 0
    queue = deque([company])
    # create a queue and add the company to it
    while queue:
        # while the queue is not empty
        current = queue.popleft()
        # get the first city from the queue
        # current is the current city
        for neighbor in graph[current]:
            # for each neighbor of the current city
            if distances[neighbor] == -1:
                # if the neighbor has not been visited
                queue.append(neighbor)
                # add the neighbor to the queue
                distances[neighbor] = distances[current] + 1
                # set the distance from the company to the neighbor to the distance from the company to the current city + 1

    result = []
    # create a list to store the result
    for i in range(1, city_nodes + 1):
        # for each city
        if i != company and distances[i] != -1:
            # if the city is not the company and has been visited
            result.append((distances[i], i))
            # add the city and its distance to the result
    result.sort(key=lambda x: (x[0], x[1]))
    # sort the result by distance and then by city
    return [x[1] for x in result]
    # return the list of cities in the result

def test_order():
    city_nodes = 5
    city_from = [1, 1, 2, 3, 1]
    city_to = [2, 3, 4, 5, 5]
    company = 1
    assert order(city_nodes, city_from, city_to, company) == [2, 3, 5, 4]
    print("All test cases passed!")


if __name__ == "__main__":
    test_order()

