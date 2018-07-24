"""https://github.com/hogeschool/INFDEV02-2"""
class Empty:
    def __init__(self):
        self.IsEmpty = True
empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

def CountList(list_name):
    cnt = 0
    while list_name.IsEmpty == False:
          cnt += 1
          list_name = list_name.Tail
    return cnt

list = Node(932, Node(33, Node(572, Node(993, empty))))
 
print(CountList(Node(932, Node(33, Node(572, Node(993, empty))))))

while list.IsEmpty == False:
    print(list.Value)
    list = list.Tail




