import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority Queue: (f_score, current_node, path, current_g_score)
    # We use f_score as the first element so heapq sorts by it automatically
    frontier = [(heuristics[start], start, [start], 0)]
    
    # Track the best (lowest) g_score found for each node
    visited = {start: 0}

    while frontier:
        # Pop the node with the lowest f_score: f(n) = g(n) + h(n)
        f, current_node, path, g = heapq.heappop(frontier)

        # Goal Check
        if current_node == goal:
            return path, g

        # Explore Neighbors
        for neighbor, weight in graph.get(current_node, []).items():
            new_g = g + weight
            
            # If we found a shorter path to this neighbor, or haven't seen it
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                f_new = new_g + heuristics.get(neighbor, 0)
                heapq.heappush(frontier, (f_new, neighbor, path + [neighbor], new_g))

    return None, float('inf')  # Return if no path exists

# --- Example Lab Data ---
adj_list = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 4},
    'C': {'D': 1},
    'D': {'Goal': 2}
}

h_values = {'A': 5, 'B': 3, 'C': 2, 'D': 1, 'Goal': 0}

path, cost = a_star_search(adj_list, h_values, 'A', 'Goal')
print(f"Path: {path} \nTotal Cost: {cost}")
