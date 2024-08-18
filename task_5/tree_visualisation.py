import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [visited_nodes.get(node[0], '#ffffff') for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_visualize(root):
    if not root:
        return

    stack = [root]
    visited_nodes = {}
    total_steps = count_nodes(root)
    step = 0

    while stack:
        current_node = stack.pop()
        visited_nodes[current_node.id] = generate_color(step, total_steps)
        step += 1

        draw_tree(root, visited_nodes)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

def bfs_visualize(root):
    if not root:
        return

    queue = deque([root])
    visited_nodes = {}
    total_steps = count_nodes(root)
    step = 0

    while queue:
        current_node = queue.popleft()
        visited_nodes[current_node.id] = generate_color(step, total_steps)
        step += 1

        draw_tree(root, visited_nodes)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

def generate_color(step, total_steps):
    start_color = (100, 0, 100)
    end_color = (144, 238, 144)

    def interpolate_color(start, end, factor):
        return tuple(int(start[i] + (end[i] - start[i]) * factor) for i in range(3))
    
    factor = step / total_steps
    color = interpolate_color(start_color, end_color, factor)
    
    return "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def build_heap_tree(heap):
    if not heap:
        return None
    
    root = Node(heap[0])
    nodes = [root]
    
    for i in range(1, len(heap)):
        node = Node(heap[i])
        parent = nodes[(i - 1) // 2]
        
        if i % 2 == 1:
            parent.left = node
        else:
            parent.right = node
            
        nodes.append(node)
    
    return root

heap = [10, 15, 20, 17, 25, 30, 40, 18]
root = build_heap_tree(heap)

print("Обход в глубину (DFS):")
dfs_visualize(root)

print("Обход в ширину (BFS):")
bfs_visualize(root)