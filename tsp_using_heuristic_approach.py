import sys
def tsp(graph, start=0):
    num_nodes=len(graph)
    visited=[False]*num_nodes
    path=[start]
    visited[start]=True
    while len(path)<num_nodes:
        current_node=path[-1]
        min_distance=sys.maxsize
        nearest_neighbor=None
        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor]<min_distance:
                nearest_neighbor=neighbor
                min_distance=graph[current_node][neighbor]
        if nearest_neighbor is not None:
            visited[nearest_neighbor]=True
            path.append(nearest_neighbor)
    path.append(start)
    return path
graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
optimal_path=tsp(graph)
print("Optimal Path:",optimal_path)
total_distance=sum(graph[optimal_path[i-1]][optimal_path[i]] for i in range(1,len(optimal_path)))
print("Total Distance:",total_distance)