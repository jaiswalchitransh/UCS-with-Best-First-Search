# UCS with Best-First Search

from queue import PriorityQueue

iteration = 1
gid = 0


class Node:
    def __init__(
        self, state, depth=0, parent=None, id=0, path_cost=0, cumulative_distance=0
    ):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.id = id
        self.path_cost = path_cost
        self.cumulative_distance = cumulative_distance

    def expand(self, problem):
        return [
            Node(
                successor,
                self.depth + 1,
                self,
                path_cost=cost,
                cumulative_distance=self.cumulative_distance + cost,
            )
            for successor, cost in problem.get_successors(self.state)
        ]

    def __lt__(self, other):
        return (self.cumulative_distance, self.id) < (
            other.cumulative_distance,
            other.id,
        )

    def __eq__(self, other):
        return (self.cumulative_distance, self.id) == (
            other.cumulative_distance,
            other.id,
        )


class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def get_successors(self, state):
        # Define the map of Romania
        romania_map = {
            "Arad": [("Sibiu", 140)],
            "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
            "Oradea": [("Sibiu", 151)],
            "Sibiu": [
                ("Arad", 140),
                ("Fagaras", 99),
                ("Oradea", 151),
                ("Rimnicu-Vilcea", 80),
            ],
            "Rimnicu-Vilcea": [("Sibiu", 80), ("Pitesti", 97)],
            "Pitesti": [("Rimnicu-Vilcea", 97), ("Bucharest", 101)],
            "Bucharest": [("Fagaras", 211), ("Pitesti", 101)],
        }
        return romania_map.get(state, [])


# Uniform Cost Search implementation
def uniform_cost_search(problem, display=False):
    return best_first_graph_search(
        problem, lambda node: node.cumulative_distance, display
    )


def best_first_graph_search(problem, f, display):
    frontier = PriorityQueue()
    node = Node(problem.initial)
    frontier.put((f(node), node))
    explored = []
    global iteration, gid

    print("\n**** Uniform Cost Search On Romania ****\n")
    print("Dictionary".ljust(30), "Priority Queue")
    while frontier:
        for (
            state,
            parent_state,
            path_cost,
            eval_function,
            cumulative_distance,
        ) in explored:
            formatted_parent = (
                f" ({parent_state})" if parent_state is not None else "()"
            )
            print(f"{state}{formatted_parent} {cumulative_distance}")

        for i, (priority, n) in enumerate(
            sorted(list(frontier.queue), key=lambda x: x[1].id), start=1
        ):
            parent_state = n.parent.state if n.parent else ""
            formatted_parent = (
                f" ({parent_state})" if parent_state is not None else "()"
            )
            eval_function = n.cumulative_distance + f(n)
            print(
                f"{n.state}{formatted_parent} {n.cumulative_distance:>}".ljust(30),
                f"#{n.id:>} {n.state:>} {priority:>}",
            )

        print("-" * 60, "")

        priority, node = frontier.get()
        eval_function = node.cumulative_distance + f(node)
        explored.append(
            (
                node.state,
                node.parent.state if node.parent else None,
                node.path_cost,
                eval_function,
                node.cumulative_distance,
            )
        )

        print(f"Processing #{node.id} {node.state} {priority}\n")
        if problem.goal_test(node.state):
            return node

        for child in node.expand(problem):
            child_state = child.state
            parent_state = child.parent.state if child.parent else None

            if node.parent is None or child_state != node.parent.state:
                gid += 1
                child.id = gid
                frontier.put((f(child), child))
        iteration += 1

    return None


# Find the shortest path.
def get_path_and_distance(node):
    path = []
    distance = 0
    while node:
        path.insert(0, node.state)
        if node.parent:
            for successor, cost in Problem(None, None).get_successors(node.state):
                if successor == node.parent.state:
                    distance += cost
        node = node.parent
    return path, distance


# Find the shortest path from Arad to Bucharest
initial_state = "Arad"
goal_state = "Bucharest"
problem = Problem(initial_state, goal_state)
result = uniform_cost_search(problem)
if result:
    path, distance = get_path_and_distance(result)
    print(f"Goal reached in {iteration} iterations:\n", end="")
    print("Shortest Path : ", " --> ".join(path))
    print("Shortest Distance : ", distance, "km\n")
else:
    print(f"\nNo path found from {initial_state} to {goal_state}.")
