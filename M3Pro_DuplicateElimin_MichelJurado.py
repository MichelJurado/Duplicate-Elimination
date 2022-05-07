# Create a function that receives a list and returns a possibly shorter
# list containing only the unique values in sorted order.
# 9/16/21
# CSC-121 M3HW1 – Duplicate Elimination
# Michel Jurado

#Part 1 Page 202 Exercise 5.7

#create a list with 10 numbers
#if numbers repeat keep only the original
#sort the list in order

Part1List1= [10,10,10,5,5,6,6,2,2,1] #creating list

def orderlist():
    """Takes list and prints out original numbers"""
    Part1List1
    noduplist=[] #creating no duplication list
    for i in Part1List1:
        if i not in noduplist: #checks if it has number in list if it does it appends it, if not doesn't 
            noduplist.append(i)
            noduplist.sort()

    print(noduplist)

#Calling Part1

print("Part 1-------")
print('\t')
print(f'Original list: {Part1List1}')
print('\t')
print("No duplicate list in order:")
orderlist()


#Part 2
#Instead of hard coding the list passed to the sorting functions, request list values from user.
#Request two lists from user, one containing numbers and another containing string
#Keep same requirements as part 1

length=5 #keeping list to five numbers
Part2List1=[]
Part2List2=[]

def Part2OrderList1():
    """Will take user inputed numbers and sort like in Part1"""
    for i in range(length):
        numbers= input("Enter 5 numbers: ")
        Part2List1.append(numbers)
        noduplist=[]
        for i in Part2List1:
            if i not in noduplist: #checks if it has number in list if it does it appends it, if not doesn't 
                noduplist.append(i)
                noduplist.sort()
    print(noduplist)

def Part2OrderList2():
    """Will take user inputed words and sort like in Part1"""
    for i in range(length):
        words= input("Enter 5 words: ")
        Part2List2.append(words)
        noduplist=[]
        for i in Part2List2:
            if i not in noduplist: #checks if it has number in list if it does it appends it, if not doesn't 
                noduplist.append(i)
                noduplist.sort()
    print(noduplist)

#calling Part2
Part2OrderList1()
Part2OrderList2()