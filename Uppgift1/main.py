#Assignment1
print("-------------------------------1")
x = 5*2
if (x < 12):
    print("true")

if(55 > 22):
    print("true")

x = 16/4
if(x == 4):
    print("true")

x = 8+2
if(x != 128):
    print("true")

x = 32*8
if(255 <= x):
    print("true")

print("-------------------------------2")
#Assignment2
#Count characters minus blankspace.
name = "Sherlock Holmes"
num_of_chars = len(name) - name.count(' ')
print(num_of_chars)

print("-------------------------------3")
#Assignment3
#Merges the parts and changes the Integers to Strings.
part_1 = "The area of a Triangle with a width of "
part_2 = 12
part_3 = " and a height of "
part_4 = 8
part_5 = " is: "
part_6 = 8*12/2
"%02d:%02d:%02d" % (part_2, part_4, part_6)
all_parts = part_1 + str(part_2) + part_3 + str(part_4) + part_5 + str(part_6)
print(all_parts)

print("-------------------------------4")
#Uppgitft4
#Prints the choosen characters in each String. Also makes them to upper/ lower digits.
word1 = "Tisdag"
word2 = "Hamburgare"
word3 = "I'll be back"
print(word1[0:3])
print(word2[3:10])
print(word3[5:12])

word4 = "It's Learning"
word5 = "Python: The Good Parts"
print(word4[5:14].upper())
print(word5[12:23].lower())

print("-------------------------------5")
#Uppgift5
#Calculates a triangle based on numbers sent to the function.
def calculate_triangle_area(height, width):
    sum = height*width/2
    print(sum)

calculate_triangle_area(12, 8)

print("-------------------------------6")
#Uppgift6
#Prints out the smallest number.
def calculate_min(x, y):
    if(x < y
    or (y > x)
    ):
        print (x)
    else:
        print(y)

calculate_min (12, 17)
#Prints out the largest number.
def calculate_max(x, y):
    if(x > y
    or (y < x)
    ):
        print (x)
    else:
        print (y)

calculate_max (12, 17)

print("-------------------------------7")
#Uppgift7
#Checks to see if a number is divisible by 2 or not.
def calculate_ifEven(num):
    if (num%2) != 0:
        print ("False")
    else:
        print("True")

calculate_ifEven (10)
