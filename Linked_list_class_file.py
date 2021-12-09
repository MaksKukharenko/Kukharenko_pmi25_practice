def insert_integer_element(element):
    j = 0
    while j < 1:
        try:
            int(element)
        except ValueError:
            element = input('Bad. Insert new good element ')
        else:
            j += 1
            element = int(element)
    return(element)

def insert_float_element(element):
    j = 0
    while j < 1:
        try:
            float(element)
        except ValueError:
            print('Wrong element type.')
            element = input('Insert new element ')
        else:
            j += 1
            element = float(element)
    return(element)

class Node:
   def __init__(self, dataval = None):
      self.data = dataval
      self.next_value = None

class LinkedList:
   def __init__(self):
      self.head_value = None

   def listprint(self):
      print_value = self.head_value
      while (print_value != None):
         print(print_value.data)
         print_value = print_value.next_value
   
   def Size(self):
    temp = self.head_value
    count = 0 
    while (temp):
        count += 1
        temp = temp.next_value
    return count

   def Add_at_begining(self, newdata):
      NewNode = Node(newdata)
      NewNode.next_value = self.head_value
      self.head_value = NewNode

   def Add_in_between(self, newdata, position):  
     while ((position > self.Size())or(position < 1)):
         position = "a"
         position = insert_integer_element(position)
     NewNode = Node(newdata) 
     if (position == 1):
       NewNode.next_value = self.headhead_value
       self.head_value = NewNode
     else:    
       temp = self.head_value
       for i in range(1, position-1):
         if(temp):
           temp = temp.next_value   
       if(temp):
         NewNode.next_value = temp.next_value
         temp.next_value = NewNode  
       else:
         print("\nThe previous node is null.")

   def Add_at_end(self, newdata):
      NewNode = Node(newdata)
      if (self.head_value == None):
         self.head_value = NewNode
         return
      last = self.head_value
      while(last.next_value):
         last = last.next_value
      last.next_value = NewNode

   def Remove_Node(self, RemoveKey):
      HeadValue = self.head_value 
      if (HeadValue):
         if (HeadValue.data == RemoveKey):
            self.head_value = HeadValue.next_value
            HeadValue = None
            return
      while (HeadValue):
         if HeadValue.data == RemoveKey:
            break
         previous = HeadValue
         HeadValue = HeadValue.next_value
      if (HeadValue == None):
         return

      previous.next = HeadValue.next_value
      HeadValue = None

   def getNth(self, i):
      temp = self.head_value
      index = 0
      while (temp):
          if (index == i):
              return temp.data
          index += 1
          temp = temp.next_value