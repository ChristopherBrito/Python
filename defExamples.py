#def are basically classes from java
#Ex.1
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
    
def main():        #Creates the main class, but doesn't execute it
    x = add(3, 2)
    y = subtract(10, 9)
    z = multiply(4, 5)
    print("Addition:", x)
    print("Subtraction:", y)
    print("Multiplication:", z)
    
main() #This executes def main.

print()#Ex.2

hunger = input("Are you hungry? Type yes if true and no if not.\n")

while hunger == "yes":
    hunger = input("Then eat some cereal. If you are still hungry type yes,"
    "if not type no.\n")

    if hunger == "no":

        print("Hope you enjoyed your meal")

        break
    
print()#Ex.3

for i in range(5):
    i += 1
    print(i)
    
print()    

num = int(input("Type in a number: "))
for i in range(num):
    print("A code has run")
 
print() 
    
for i in range(6):
    if i<4:
        print(">")
    else:
        print("<")
        
print()#Ex.4

print("For the following few inputs, follow the directions.")

input("The type is a string: ")

int(input("The type is an integer: "))

float(input("The type is a float: "))

bool(input("The type is a boolean variable: "))

    

    
