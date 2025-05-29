class Node:
    def __init__(self, val=0, neighbours=None):
        self.val = val
        self.neighbours = []
    
    def add_neighbour(self, neighbour_node):
        self.neighbours.append(neighbour_node)
    
    def remove_neighbour(self, neighbour_node):
        self.neighbours.remove(neighbour_node)

    def __str__(self):
        return f"Value: {self.val}, neighbours: {self.neighbours}"



