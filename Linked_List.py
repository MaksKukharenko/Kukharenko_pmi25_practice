from Linked_list_class_file import *
import random

MyList = LinkedList()
exit = 0

while(exit == 0):
   print("Print option: \n1)Generate random elements\n2)Add element\n3)Delete element\n4)Task\n5)Exit")
   answer = int(input("I choose "))
   answer = insert_integer_element(answer)
   if (answer == 1):
      print("Insert a and b:")

      a = input("a = ")
      a = insert_integer_element(a)

      b = input("b = ")
      b = insert_integer_element(b)

      n = input("How many elements?")
      n = insert_integer_element(n)

      MyList.head_value = Node(random.randint(a, b))
      for i in range(n - int(1)):
         MyList.Add_at_end(random.randint(a, b))
   elif (answer == 2):
      element = input("What would you like to add? ")
      element = insert_float_element(element)
      position = input("On what position? ")
      if (position == "head"):
         MyList.Add_at_begining(element)
      elif (position == "end"):
         MyList.Add_at_end(element)
      else:
          position = insert_integer_element(position)
          MyList.Add_in_between(element, position)
      MyList.listprint()
   elif (answer == 3):
      element = input("What would you like to remove? ")
      element = insert_float_element(element)
      MyList.Remove_Node(element)
   elif (answer == 4): #This doesn't work
      maximum = -9999999
      size = MyList.Size()
      print("Size = ",MyList.getNth(size - i))
      for i in range(1, int(round(MyList.Size()/2))):
          if (maximum < float(MyList.getNth(1 - i)) + float(MyList.getNth(size - i - 1))):
              maximum = float(MyList.getNth(1 - i)) + float(MyList.getNth(size - i))
      print("Max = ", maximum)
      #print("Goodbye, World")
   elif (answer == 5):
       exit = 95
       print("Goodbye")
   else:
       print("Wrong answer")
   MyList.listprint()