class Node:
    def __init__(self, val=0, neighbours=None):
        self.val = val
        self.neighbours = []
    
    def add_neighbour(self, neighbour_node):
        self.neighbours.append(neighbour_node)
    
    def remove_neighbour(self, neighbour_node):
        self.neighbours.remove(neighbour_node)




