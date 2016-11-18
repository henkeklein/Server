#Uppgift1
print("-------------------------------1")
def printNumbers(num):
    for i in range(num):
        print(i)
printNumbers (10)

print("-------------------------------2")
#Uppgift2
def fooBar(num):
    i = 1
    while i < num+1:
        answer = ""
        if (i%3 == 0):
            answer += "Foo"
        if (i%5 == 0):
            answer += "Bar"

        if(answer):
            print(answer)
        else:
            print(i)
        i=i+1
fooBar(15)

print("-------------------------------3")
#Uppgift3
#Returns the sum / numbers in array.
def calculate_average(num):
    return float(sum(num)) / max(len(num), 1)

numbers = [1, 2, 3, 4]
average = calculate_average(numbers)
print(average)

print("-------------------------------4")
#Uppgift4
def filter_names_by_length(names, length):
    index = []
    for name in names:
        if len(name) > length:
            index.append(name)
    return index

# List of names
names = ["Sherlock", "John", "Eliza", "Joe", "Watson"]

# All names that have more then 4 characters
names_above_4 = filter_names_by_length(names, 4)
print(names_above_4) # => ["Sherlock", "Eliza", "Watson"]

# All names that have more then 6 characters
names_above_6 = filter_names_by_length(names, 6)
print(names_above_6) # => ["Sherlock"]

print("-------------------------------5")
#Uppgift5
    # Dictionary
myself = {"firstname": "Sherlock", "lastname": "Holmes", "age": 35, "top_3_movies": ["Seven", "Gone Girl", "The Prestige"]}

# Firstname - String
print(myself["firstname"])
# eg. => "Sherlock"

# Lastname - String
print(myself["lastname"])
# eg. => "Holmes"

# Age - Integer
print(myself["age"])
# eg. => 35

# Movies - List
print(myself["top_3_movies"])
# eg. => ["Seven", "Gone Girl", "The Prestige"]

print("-------------------------------6")
#Uppgift6
def printPerson(obj):
    if type (obj) == dict:
        age = '(' + str(obj["age"]) + ')'
        movies = ', '.join(obj["top_3_movies"])
        print(obj["firstname"] + " "+ obj["lastname"] + " " + age + ", Top Movies: " + movies)

person = {
    "firstname": "Sherlock",
    "lastname": "Holmes",
    "age": 35,
    "top_3_movies": ["Seven", "Gone Girl", "The Prestige"]

}
printPerson(person)

print("-------------------------------7")
#Uppgift7
def createPerson(firstname, lastname, age, top_3_movies):
    age = '(' + str(age) + ')'
    movies = ', '.join(top_3_movies)
    print(firstname + " " + lastname + " "+ age + ", Top Movies: " + movies)

sherlock = createPerson("Sherlock", "Holmes", 35, ["Seven", "Gone Girl", "The Prestige"])

printPerson(sherlock)
