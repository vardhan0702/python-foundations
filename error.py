#with try and except block
try:
    result =10/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
print("Program continues to run after handling the exception." )

print("--------------------------------------------")
# without try and except block
#result1 = 5 / 0
#print(result1)

#catching different types of errors separately.
try:
    value = 12/0
except ValueError:
    print("Error: Invalid value. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("--------------------------------------------")


print("#implement this try and except while reading files.")
#implement this try and except while reading files.

try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")