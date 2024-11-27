import heapq
class Node:
    def __init__(self, name, heuristic):
        self.name, self.heuristic, self.neighbors = name, heuristic, []
    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))
def a_star_search(start, goal):
    open_list = [(0, start.name, start)]
    came_from, g_score = {}, {start: 0}
    while open_list:
        _, _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current.name)
                current = came_from[current]
            return path[::-1] + [goal.name], g_score[goal]
        for neighbor, weight in current.neighbors:
            new_score = g_score[current] + weight
            if new_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor], g_score[neighbor] = current, new_score
                heapq.heappush(open_list, (new_score + neighbor.heuristic, neighbor.name, neighbor))
    return None, float('inf')
nodes, edges = {}, input("Nodes and heuristics (e.g., 'A 1 B 2'): ").split()
for i in range(0, len(edges), 2):
    nodes[edges[i]] = Node(edges[i], float(edges[i+1]))
edges = input("Edges and weights (e.g., 'A B 1 B C 2'): ").split()
for i in range(0, len(edges), 3):
    nodes[edges[i]].add_neighbor(nodes[edges[i+1]], float(edges[i+2]))
    nodes[edges[i+1]].add_neighbor(nodes[edges[i]], float(edges[i+2]))
start, goal = nodes[input("Start node: ")], nodes[input("Goal node: ")]
path, cost = a_star_search(start, goal)
print(f"Path: {' -> '.join(path)}\nCost: {cost}" if path else "No path found")
