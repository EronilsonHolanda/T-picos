
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.childLeft = None
        self.childRight = None
    #}__init__
    def bfs(self, value):
        if self.childLeft is not None:
            if self.childLeft.value == value:
                return self.childLeft
        if self.childRight is not None:
            if self.childRight.value == value:
                return self.childRight
        if self.childLeft is not None:
            self.childLeft.bfs(value)
        if self.childRight is not None:
            self.childRight.bfs(value)
    def print(self):
        print(f"  {self.value}  ")
        if self.childLeft is not None:
            self.childLeft.print()
        if self.childRight is not None:
            self.childRight.print()
#}class Node