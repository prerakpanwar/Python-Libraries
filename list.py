# # reversing a string
# a = 'abcdef'
# print (a[: :-1])

# #list functions
# a_list = [2,4,6,8,10,2]

# print(len(a_list))
# print(min(a_list))
# print(max(a_list))
# print(sum(a_list))
# print(sum(a_list)/len(a_list))


# #checking for an element using IN & NOT IN
# if (8 in a_list):
#     print('Element exists')
# else:
#     print('Not exists')

# if (8 not in a_list):
#     print('Element exists')
# else:
#     print('Not exists')

# print(a_list.count(2))
# x = a_list.reverse()
# print(f'new reversed list is : {a_list}')
# y = a_list.sort()
# print(f'new sorted list is : {a_list}')

#removing elements from list
b_list = [1,3,5,7,9]
del(b_list[1])
print(b_list)


z = b_list.pop()
print(f'popped element is: {z}')
print(f'new list is: {b_list}')

#copy VS modifying
#copy
c_list = [1,2,3]
d_list = c_list.copy()  #OR -> d_list = c_list[:]
c_list.append(4)
print(c_list)
print(d_list) 

#modifying
c_list = [1,2,3]
d_list = c_list
c_list.append(4)
print(c_list)
print(d_list) 

#Shallow copy VS Deep copy
#Shallow copy means that any changes made to a copy of an object do reflect in the original object.
#Deep copy means that any changes made to a copy of the object do not reflect in the original object. 

list1 = [1,2,3]                        # Make a list

list2 = ["List within a list", list1]  # Nest it in another list

list3 = list2.copy()                   # Shallow copy list2

print("Before appending to list1:")
print("List2:", list2)
print("List3:", list3, "\n")

list1.append(4)                        # Add an item to list1
print("After appending to list1:")
print("List2:", list2)
print("List3:", list3)


import copy                            # Load the copy module

list1 = [1,2,3]                        # Make a list

list2 = ["List within a list", list1]  # Nest it in another list

list3 = copy.deepcopy(list2)           # Deep copy list2

print("Before appending to list1:")
print("List2:", list2)
print("List3:", list3, "\n")

list1.append(4)                        # Add an item to list1
print("After appending to list1:")
print("List2:", list2)
print("List3:", list3)


