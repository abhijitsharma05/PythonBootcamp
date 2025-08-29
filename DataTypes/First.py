
integer_number = 30.89
floating_number = 3.14566
complex_number = 3 +7j
 
is_active = True
text = "Hello, World!"    # text or String
empty_value = None
 
print("This is the int value with: ", integer_number , " ->" , type(integer_number))
print("This is the complex value ", complex_number , " ->" , type(complex_number))
 
print("This is the value", is_active , " ->" , type(is_active))
print("This is thevaue  ", empty_value , " ->" , type(empty_value))
print("\n" + "-"*50 + "\n")
 
# Below are the complex types
numbers = [45,36,78,89,23]    # list
coordinates = (10.0, 20.0)    # tuple
unique_numbers = {1, 2, 3, 4, 5, 2, 4}    # set = no duplicate values
person = {"name": "John", "age": 30}    # dictionary = key-value pairs
print(numbers)
 
samplefrozenSet = frozenset(unique_numbers)   # frozenset = immutable set
print(samplefrozenSet)
 
 #------------------------------

is_bool = True

number = {1,2,3,4,5}
print(type(number))

number = (1,2,3,4,5)
print(type(number))

number = [1,2,1,3,4,5]
print(type(number), number)

number = {1,2,3,4,1,5}
number.add(10)
print(type(number), number)


r = list(range(0,12,2))
print(r)

print("\n" + "-"*50 + "\n")

grocery = ["bread", "milk", "eggs", "butter","Buns","curd","12"]  # list of grocery items
print("Grocery List:", grocery)
grocery.sort()
print("Grocery List:", grocery)
 
# replcaing the element in the list
index = grocery.index('butter')
print("Index of 'butter':", index)
grocery[index] = 'jam'  # updating butter to jam
print("Updated Grocery List:", grocery)
 
grocery.pop()   # pop will remove the lst item from the list
print("Grocery List after pop():", grocery)
 
grocery.extend(['cookies', 'chocolates','milk'])  # adding multiple items to the list
print("Grocery List after extend():", grocery)
 
backup_list = grocery.copy()  # copying the list
print("Copied Grocery List:", backup_list)
 
changed_list = [item.upper() for item in grocery]   # list comprehension to convert items to uppercase
print("Changed Grocery List to Uppercase:", changed_list)
 
print("First item in the grocery list:", grocery[0])  # accessing the first item
print("Last item in the grocery list:", grocery[-1])  # accessing the last item
 
print("Number of items in the grocery list:", len(grocery))  # length of the list
 
print("first two items, grocery[:2]", grocery[:2])
 
grocery.insert(2, 'rice')  # inserting 'rice' at index 2
print("Grocery List after insert():", grocery)
 
grocery.remove('milk')  # removing 'milk' from the list
print("Grocery List after remove():", grocery)
 
del grocery[3]  # deleting item at index 3
print("Grocery List after del:", grocery)
 
print("is eggs are there in the list or not?", 'eggs' in grocery)  # checking if 'eggs' is in the list
 
grocery.extend(['milk', 'chocolates','milk'])
print("Number of times 'milk' appears in the list:", grocery.count('milk'))  # count occurrences of 'milk'
 
grocery.reverse()  # reversing the list
print("Reversed Grocery List:", grocery)
 
grocery.clear()  # clearing the list
print("Cleared Grocery List:", grocery)
 
#-----------------------------------------------------
print("Cricket score")

score = []
score.extend(['85', '90', '78', '92', '88'])
print(score)

score.insert(2, '80')
print("inserted 80 at index 2", score)

score.remove("92")
print(score)

score.sort()
print("sorted in ascending",score)

score.reverse()
print("reversed list",score)

print("maximum score", max(score))
print("minimum score", min(score))

for i in score:
    if i == "90":
        print("Is 90 Present: ",True)


print("total number of score",len(score))

print("first 3 scores",score[:3])

print("remove last score",score[-1])

score[2] = 95
print("replacing index 2 with 95:",score)

copied_score = score.copy()
print("copied score",copied_score)


#2nd
NewScore = 75
if NewScore > 90:
    grade = "A"
elif NewScore > 80:
    grade = "B"
elif NewScore > 70:
    grade = "C"
elif NewScore > 60:
    grade = "D"
else:
    grade = "E"
print(grade)

#3rd


