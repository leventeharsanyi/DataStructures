from heapq import heappush, heappop

def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str) -> dict[str, float]:
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        curr_dist, curr_node = heappop(heap)
        if curr_dist > distances[curr_node]:
            continue
        for next_node, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heappush(heap, (new_dist, next_node))
    return distances

def dijkstra_path(graph: dict[str, list[tuple[str, int]]], start: str, target: str) -> tuple[float, list[str]]:
    distances = {node: float("inf") for node in graph}
    previous = {node: "None" for node in graph}  ## extra

    distances[start] = 0
    heap = [(0, start)]
    while heap:
        curr_dist, curr_node = heappop(heap)
        if curr_dist > distances[curr_node]:
            continue
        for next_node, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                previous[next_node] = curr_node ## extra
                heappush(heap, (new_dist, next_node))

    path = []
    node = target
    while node != "None":
        path.append(node)
        node = previous[node]
    path.reverse()

    return distances[target], path

if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 2), ("D", 4)],
        "B": [("A", 1), ("F", 6), ("E", 5)],
        "C": [("A", 2), ("D", 1), ("H", 4)],
        "D": [("A", 4), ("C", 1), ("I", 5)],
        "E": [("B", 5), ("F", 1), ("G", 2)],
        "F": [("B", 6), ("E", 1), ("G", 3)],
        "G": [("E", 2), ("F", 3), ("H", 4), ("L", 3)],
        "H": [("C", 4), ("G", 4), ("J", 2)],
        "I": [("D", 5), ("J", 6)],
        "J": [("H", 2), ("I", 6), ("K", 1)],
        "K": [("J", 1), ("L", 4), ("M", 1)],
        "L": [("G", 3), ("K", 4), ("M", 2)],
        "M": [("K", 1), ("L", 2)]
    }
    print(dijkstra(graph, "A"))
    print(dijkstra_path(graph, "A", "M"))
    print(dijkstra_path(graph, "A", "E"))