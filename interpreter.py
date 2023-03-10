example = input ("Expression: ")
example = example.split()
x = float(example[0])
y = example[1]
z = float(example[2])
if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y== "*":
    print(x*z)
else:
    print(x/y)   
