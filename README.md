# UCS with Best-First Search

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contribution](#contribution)


## Project Overview
This Python script implements Uniform Cost Search (UCS) with Best-First Search to find the shortest path from the city of Arad to Bucharest in Romania. It utilizes classes and functions to represent nodes, the problem, and search algorithms.
The `Node` class represents a node in the search tree with attributes such as state, depth, parent, id, path cost, and cumulative distance. It includes an `expand()` method to generate child nodes based on the problem's successor function.
The `Problem` class initializes the problem with the initial state (Arad) and the goal state (Bucharest). It includes methods `goal_test()` to check if a state is the goal state and `get_successors()` to provide successors for a given state based on the map of Romania.


## Installation
This project requires Python 3.12.1 or later.
To set up the project:
1. Ensure Python 3.12.1 or a later version is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository to your local machine.

            git clone https://github.com/jaiswalchitransh/UCS-with-Best-First-Search.git

3. Open the project in your preferred Python environment (e.g., IDE or terminal).
4. Run the script (`UCS.py`) and observe the output to see the valid coloring of regions.


## Usage
Run the script:

            python UCS.py
  
This executes the UCS with Best-First Search algorithm to find the shortest path from Arad to Bucharest in the Romania map graph.


## Features
- **Implementation**: Implements UCS using Best-First Search for optimal pathfinding.
- **Output**: Outputs the shortest path and distance from Arad to Bucharest.
- **Demonstration**: Utilizes a priority queue for managing frontier nodes efficiently.


## Contribution
I, **Chitransh Jaiswal** developed this Project Individually. I was responsible for all aspects of the project, including design, development, testing, and documentation.
Contributions to improve the efficiency, readability, or functionality of the code are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

Please ensure your contributions adhere to the coding standards and follow the existing style and structure.

---

Thank you for your interest in the UCS with Best-First Search!
