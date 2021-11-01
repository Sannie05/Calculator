#Variabels
x = float(input("Write a number: "))
y = str(input("Write a symbol(+ - * /): "))
z = float(input("Write a number: "))
#Functions
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x // z)
input("Press enter to close the program.")