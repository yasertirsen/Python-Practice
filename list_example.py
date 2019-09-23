a = "is"
b = 2
my_list = ["my", "list", a, b]

print(my_list)

list_of_lists = [my_list, [4,5]]

print(list_of_lists)

list_of_items = [my_list, [4,5], 8]

print(list_of_items[0])
print(list_of_items[1])
print(list_of_items[2])
print(list_of_items[-3])
print(len(list_of_items))

print(list_of_items[3]) #will generate error
