import random
def insert_integer_element(element):
    j = 0
    while j < 1:
        try:
            int(element)
        except ValueError:
            print('Wrong element type.')
            element = input('Insert new element ')
        else:
            j += 1
            element = int(element)
    return(element)
def fill_matrix(n, A):
    for i in range(n):
        j = 0
        row = []
        element = 0
        while j < int(n):
            element = input()
            try:
                int(element)
            except ValueError:
                print('Wrong element type.')
            else:
                row.append(int(element))
                j += 1
        A.append(row)
def fill_random_matrix(n, A, start, end):
    for i in range(n):
        j = 0
        row = []
        while j < int(n):
            row.append(int(random.randint(start, end)))
            j += 1
        A.append(row)
def print_matrix(n, A):
    for i in range(n):
       for j in range(n):
          print(A[i][j], end=' ')
       print('')

end = 0
while end != 1:
    answer = n = 0
    matrix = []
    print("Hello, user. What do you want to do?\n1) Fill NxN matrix\n2) Generate NxN matrix using elements between a and b\n3) Exit")
    while answer < 1 or answer > 3:
        answer = input()
        answer = insert_integer_element(answer)
    if answer == 3:
        end = 1
        print('Goodbye')
        continue
    if answer != 3:
        n = input("Input N: ")
        n = insert_integer_element(n)
    if answer == 1:
        fill_matrix(n, matrix)
        print_matrix(n, matrix)
    if answer == 2:
        print("Input a: ")
        a = input()
        a = insert_integer_element(a)
        print("Input b: ")
        b = input()
        b = insert_integer_element(b)
        fill_random_matrix(n, matrix, a, b)
        print_matrix(n, matrix)
        print("B")
        sort_matrix(n, matrix)
