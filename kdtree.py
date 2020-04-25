from collections import namedtuple
from operator import itemgetter
from pprint import pformat
import pydot
from IPython.display import Image,display
from graphics_turtle import create

class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))


def draw_tree(tree,G):
  if isinstance(tree[0], tuple):
    node = pydot.Node(str(tree[0]),style="filled",fillcolor='yellow',shape = 'box')
    G.add_node(node)

    try:
      if not isinstance(tree[1],str):
        edge = pydot.Edge(str(tree[0]),str(draw_tree(tree[1],G)))
        G.add_edge(edge)
    except IndexError:
      o=1
    try:
      if not isinstance(tree[1],str):
        edge = pydot.Edge(str(tree[0]),str(draw_tree(tree[2],G)))
        G.add_edge(edge)
    except IndexError:
      o=1
    return tree[0]

def kdtree(point_list, depth=0):
    global height
    height = 0
    if height<depth:
        height = depth
        
    if not point_list:
        return 'None'

    k = len(point_list)
    axis = depth % k
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2
    return Node(
        location=point_list[median],
        left_child=kdtree(point_list[:median], depth + 1),
        right_child=kdtree(point_list[median + 1:], depth + 1)
    )

def get_tree(point_list):
    tree = kdtree(point_list)
    return tree

def main(point_list):
    """Example usage"""
    tree = kdtree(point_list)
    create(tree,height)
    
    G= pydot.Dot(graph_type='digraph')
    node = pydot.Node(str(tree[0]),style="filled",fillcolor='green',shape = 'box')
    G.add_node(node)
    edge = pydot.Edge(str(tree[0]),str(draw_tree(tree[1],G)))
    G.add_edge(edge)
    edge = pydot.Edge(str(tree[0]),str(draw_tree(tree[2],G)))
    G.add_edge(edge)
    G.write_png('Graph.png')
    
    
    

if __name__ == '__main__':
    main(point_list)
