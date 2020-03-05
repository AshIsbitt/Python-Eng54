def get_val():
    vals = []
    vals.append(int(input("Enter first number: ")))
    vals.append(int(input("Enter second number: ")))

    return vals


def add_num(num1, num2):
    return num1 + num2


def sub_num(num1, num2):
    return num1 - num2


def multiply_num(num1, num2):
    return num1 * num2

def div_num(num1, num2):
    return num1 / num2


def circle():
    rad = float(input("Input radius: "))
    return rad * rad * 3.14


def square():
    val1 = float(input("Enter first value: "))
    val2 = float(input("Enter second value: "))

    return val1 * val2


def triangle():
    h = float(input("Enter height: "))
    b = float(input("Enter base: "))

    return (h * b) / 2


def area():
    shape = input("Pick a shape: Circle, Square, Triangle:\n")

    if shape.lower() == 'circle':
        print(circle())
    elif shape.lower() == 'square':
        print(square())
    elif shape.lower() == 'triangle':
        print(triangle())
    else:
        quit()


def fib(iterates):
    num1 = 0
    num2 = 1
    ret = []

    for i in range(round(iterates / 2)):
        ret.append(num1)
        num1 = add_num(num1, num2)
        ret.append(num2)
        num2 = add_num(num1, num2)

    return ret


while True:
    print("Options: Add, Subtract, Multiply, Divide, Area, Fib")
    math_feature = input("Enter function name: ")

    if (math_feature.lower() == "add" or math_feature.lower() == 'subtract' or
    math_feature.lower() == 'multiply' or math_feature.lower() == 'divide'):

        vals = get_val()
        num1 = vals[0]
        num2 = vals[1]

    if math_feature.lower() == 'add':
        print(add_num(num1, num2))

    elif math_feature.lower() == 'subtract':
        print(sub_num(num1, num2))

    elif math_feature.lower() == 'multiply':
        print(multiply_num(num1, num2))

    elif math_feature.lower() == 'divide':
        print(div_num(num1, num2))

    elif math_feature.lower() == 'area':
        area()

    elif math_feature.lower() == 'fib':
        iter = int(input("Enter number of iterations: "))
        print(fib(iter))
        print("")

    else:
        break

