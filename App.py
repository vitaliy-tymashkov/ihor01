import sys
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def printSigns():
    print("op1 " + operation1.__name__)
    print("op2 " + operation2.__name__)
    print("op3 " + operation3.__name__)
    print("op4 " + operation4.__name__)
    print("op5 " + operation5.__name__)
#
op1 = 5
op2 = 6
op3 = 8
op4 = 0
op5 = 4
op6 = 10
res = 0

operations = [add, sub, mul, div]
for o1 in operations:
    for o2 in operations:
        for o3 in operations:
            for o4 in operations:
                for o5 in operations:
                    operation1 = o1
                    operation2 = o2
                    operation3 = o3
                    if (operation3 == div):
                        break
                        #operation3 = add
                    operation4 = o4
                    operation5 = o5

                    #printSigns()
                    expression = operation5(operation4(operation3(operation2(operation1(op1, op2), op3), op4), op5), op6)
                    if (expression == res):
                        print(expression)
                        printSigns()
                        print("finish")
                        sys.exit()