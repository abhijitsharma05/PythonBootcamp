
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

#Saturday 
student = ('Ravi',34,"Delhi","India","IT","Delhi")
print("student tuple, student", student)
 
print("Nmae",student[0])
print(" address details:", student[2:4])
 
if "A" in student:     #Mmeberhsip Test
    print("A is present in the tuple")
   
for a in student:
    print("value:", a)
   
print("Length of the tuple:", len(student))
 
print(" Occuracingin the the student tuple", student.count("Delhi"))
 
print("Index of IT in the tuple:", student.index("IT"))
 
# Tuple to list conversion
student_list = list(student)
student_list.append("WIPRO Technologies")
student_list[3] = "Bangalore"
print( "The list is ", student_list)
 
# convert back to tuple fromthe list
student = tuple(student_list)
print("The modified tuple is ", student)
 
project_codes = ('P001', 'P002', 'P003') # another tuple
complete_tuple = student + project_codes  # concatenation of tuples
print("The complete tuple after concatenation is ", complete_tuple)
 
#tuple within the tuple = nested tuples
studdent_nested = (student, project_codes)
print("The nested tuple is ", studdent_nested)
print("Accessing nested tuple element:", studdent_nested[0][1])  # accessing
print("Accessing nested 2nd tuple element:", studdent_nested[1][1])  # accessing
print(student)
 
#Unpacking the tuple
name, age, city, country, dept, state, org = student
print("Unpacked Values - Name:", name, ", Age:", age, ", City:", city, ", Country:", country, ", Dept:", dept, ", State:", state)
 
scores = (56,89,23,90,87,66)
print("Minimum score:", min(scores))
print("Maximum score:", max(scores))
print("Sum of scores:", sum(scores))
 
#extended tuple unpacking
a, b, c, *rest = scores
print("a:", a)
print("b:", b)  
print("c:", c)
print("rest:", rest)  # rest will be a list of remaining elements
 
# comparision of tuples
print((3,4,5) == (3,4,5))
print((6,7,4) == (6,7,1))
 
s = list(scores)
s.sort
 
# comparision of tuples
print((3,4,5) > (3,4,5))
print((6,7,4) > (6,7,1))

#string------------------/--------------------------------/-----------------------------
 
s1 = "Samsung LED is good TV and is available in mutiple colors"
s2 = '                    Brand is good                                             '
s3 = """This is a good rband in the market
You can see multiple products of multiple categories
Available in all the major retail stores
you can buy online also.
"""
 
print([s1, s2, s3])
 
print(s1[2])
print(s1[0:6])
print(s1[0:10:2])  # step value
print(s1[-1])  # last character
print(s1[-4:])  # negative indexing including the last chafacter
print(s1[-4:-2])  # negative indexing eclusign the last character
print(s1[-5])  # negative indexing to fetch the 5th indexed character from last
print(s1[::-1])  # reversing the string
 
print("Length of the string s1:", len(s1))
 
print( s1 * 4) # repeating the string
 
print(s2.upper()) # converting to upper case
print(s2.lower()) # converting to lower case
print(s2.strip()) # removing leading and trailing spaces
print(s1.replace("is", "are")) # replacing the string
print(s3.split(" ")) # splitting the string based on space
print(s1.startswith("Sam")) # checking the starting of the string
print(s1.endswith("LED ")) # checking the ending of the string
print(s1.find("LED")) # finding the index of the substring
print(s1.count("in")) # counting the occurrence of a substring
 
v = "black, white, grey,darkblack"
res = v.split(",") # splitting the string based on comma
print(res)
x = "::".join(res) # joining the list elements with hyphen
print(x)
 
print("is" in s1) # membership test
reverse_Str = ''.join(reversed(s1)) # reversing the string using reversed() function
print(reverse_Str)
 