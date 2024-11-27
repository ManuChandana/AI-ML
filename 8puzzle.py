import heapq
class PuzzleState:
    def __init__(self, board, goal, moves=0, prev=None):
        self.board, self.goal, self.moves, self.prev = board, goal, moves, prev
        self.blank_pos = board.index('*')
    def __lt__(self, other):
        return self.cost() < other.cost()
    def cost(self):
        return self.moves + self.heuristic()
    def heuristic(self):
        return sum(abs((b // 3) - (g // 3)) + abs((b % 3) - (g % 3))
                   for b, g in ((self.board.index(str(n)), self.goal.index(str(n))) for n in range(1, 9)))
    def get_neighbors(self):
        neighbors = []
        r, c = divmod(self.blank_pos, 3)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_blank = nr * 3 + nc
                new_board = list(self.board)
                new_board[self.blank_pos], new_board[new_blank] = new_board[new_blank], new_board[self.blank_pos]
                neighbors.append(PuzzleState(tuple(new_board), self.goal, self.moves + 1, self))
        return neighbors
    def is_goal(self):
        return self.board == self.goal
    def __repr__(self):
        return '\n'.join(' '.join(self.board[i:i + 3]) for i in range(0, 9, 3))
def a_star(start):
    open_set = [(0, start)]
    visited = set()
    while open_set:
        _, current = heapq.heappop(open_set)
        if current.is_goal():
            return current
        visited.add(current.board)
        for neighbor in current.get_neighbors():
            if neighbor.board not in visited:
                heapq.heappush(open_set, (neighbor.cost(), neighbor))
    return None
def get_board(prompt):
    return tuple(input(prompt).split())
start = PuzzleState(get_board("Enter start state (e.g., '1 2 3 4 5 6 7 8 *'): "), 
                    get_board("Enter goal state (e.g., '1 2 3 4 5 6 7 8 *'): "))
solution = a_star(start)
if solution:
    path = []
    while solution:
        path.append(solution)
        solution = solution.prev
    for depth, state in enumerate(reversed(path)):
        print(f"Step {depth}:")
        print(state)
        print(f"Depth Level: {state.moves}, Heuristic Value: {state.heuristic()}\n")
else:
    print("No solution found.")
