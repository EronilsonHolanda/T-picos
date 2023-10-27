from node import Node
from tree import Tree

#        45
#    33      77
# 22        65       88
n88 = Node(88)
n65 = Node(65)
n77 = Node(77)
n22 = Node(22)
n33 = Node(33)
n45 = Node(45)

n77.childRight = n88
n88.parent = n77
n77.childLeft = n65
n65.parent = n77
n45.childLeft = n33
n33.parent = n45
n45.childRight = n77
n77.parent = n45

t = Tree()
t.root = n45

busca77 = t.bfs(45)
busca77.print()