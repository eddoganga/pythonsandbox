# a function is a block of code which only runs when it is called

#create a function

def sayHello(name):
    print(f'hello {name}')

#return values

def getSum(num1, num2):
    total= num1 + num2
    return total
print(getSum(3,4))

#lambada smaal anonymous function

getsum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))