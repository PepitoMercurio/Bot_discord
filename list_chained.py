class list_chained:
  def __init__(self, first_data):
    self.first_node = Node(first_data) 
    self.last_node = self.first_node
    self.size = 1

  def append(self,data):
    self.last_node.next_node = Node(data)
    self.last_node = self.last_node.next_node
    self.size +=1

  def insert_first(self,data):
    current_node = Node(data)
    current_node.next_node = self.first_node
    self.first_node =current_node
    self.size +=1

  def size(self):
    return self.size


  def insert(self, indice, data):
    current_node = self.first_node
    i = 0
    while indice > i:
      current_node = current_node.next_node
      i += 1
    new_node = Node(data)
    new_node.next_node = current_node.next_node
    current_node.next_node = new_node

    self.size += 1
  

class Node:
  def __init__(self,data):
    self.data = data
    self.next_node = None
    self.previous_node = None

L = list_chained(5)

class list_chained_sorted :
  def __init__(self,data):
    self.first_node = Node(data)

  def add_data(self,data) :
    N = Node(data)
    if data < self.first_node.data:
      N.next_node = self.first_node
      self.first_node = N
      return
    
    if data < self.last_node.data:
      self.last_node.next_node
      self.last_node = N
      return


    current_node = self.first_node
    while current_node.next_node.data < data :
      current_node = current_node.next_node
    
    N = Node(data)
    N.next_node = current_node.next_node
    current_node.next_node = N
    