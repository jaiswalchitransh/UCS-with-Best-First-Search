# UCS-with-Best-First-Search

The Python code implements Uniform Cost Search (UCS) to find the shortest path from the city of Arad to Bucharest in Romania. The code utilizes classes and functions to represent nodes, the problem, and search algorithms.

The Node class represents a node in the search tree with attributes such as state, depth, parent, id, path cost, and cumulative distance. It also has a method expand() to generate child nodes based on the problem's successor function.

The Problem class represents the problem to be solved, initialized with the initial state (Arad) and the goal state (Bucharest). It has a method goal_test() to check if a given state is the goal state and get_successors() to provide successors for a given state based on the map of Romania.

The uniform_cost_search() function implements the UCS algorithm. It calls best_first_graph_search() with a specific evaluation function based on the cumulative distance. The function utilizes a priority queue to manage frontier nodes and explores nodes in a best-first manner.

The best_first_graph_search() function performs the actual search. It iteratively explores nodes in the frontier, expanding them and updating the frontier accordingly until the goal state is reached or no more nodes are left to explore.

The get_path_and_distance() function retrieves the shortest path and its distance from the final node back to the initial node.

Finally, the code sets up the initial state (Arad) and the goal state (Bucharest), creates a problem instance, performs the UCS search, and prints the shortest path and distance if a solution is found. Otherwise, it indicates that no path exists between the specified cities.
