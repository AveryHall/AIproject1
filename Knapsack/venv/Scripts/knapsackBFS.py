"""
Avery Hall
CS-4453-01-Artificial Intelligence
Dr. Arisoa Randrianasolo
This program implements a solution to the knapsack problem using both DFS and BFS by reading in an input file and then
outputting a list of items selected, and their total values/weights.
"""

from collections import deque
import copy


def bfs():                    # BFS

    global max_value
    global max_weight
    global items_selected
    max_value = 0
    max_weight = 0
    items_selected = []

    init_node = Node()

    queue = deque([init_node])

    while queue:

        node = queue.popleft()

        if node.value > max_value and node.weight <= Capacity:
            max_value = node.value
            max_weight = node.weight
            items_selected = node.items

        neighbors = expand_neighbors(node)
        for j in neighbors:
            queue.append(j)

        for test in queue:
            print(test.items)

    return items_selected, max_value, max_weight


def expand_neighbors(n):

        new_neighbors = []
        temp = copy.copy(n)
        used_items = temp.items

        for num_neighbors in range(numItems - len(n.items)):
            print(num_neighbors)
            s = Node()
            s.parent = n
            s.depth = n.depth + 1

            s.items = list(n.items)

            for item in range(1, numItems + 1):
                if item not in used_items:
                    s.items.append(item)
                    s.value += values[item-1]
                    s.weight += weights[item-1]
                    used_items.append(item)
                    break

            print(used_items, s.items, s.value, s.weight)
            new_neighbors.append(s)

        return new_neighbors


def init_queue():                       # Constructs the start of the tree from the first "empty" Node
    # for j in range(0, numItems):
    return


class Node:                     # Defines Node class
    def __init__(self):
        self.parent = None
        self.depth = 0
        self.value = 0
        self.weight = 0
        self.items = []


# Output Section
# File input section
# Opens and reads from a file, then closes the file
itemInput = open('items.txt')
contents = itemInput.readlines()
itemInput.close()
# print(contents)

# Separates the file contents and does unit conversions
Capacity = int(contents[0])     # Capacity of knapsack
numItems = int(contents[1])     # Number of items that could be put into the sack
values = contents[2].split()    # A list of values for the items
weights = contents[3].split()   # A list of weights for the items
# Convert the value and weight to integers
for i in range(0, numItems):
    values[i] = int(values[i])
    weights[i] = int(weights[i])
# print(Capacity, numItems, values, weights)


print(bfs())
