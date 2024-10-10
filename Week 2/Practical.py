def Variable_assigment():
    total = 100
    print("The total is", total)

    total += 99
    print("The new total is", total)

    total -= 98
    print("The total is", total)
    total *= 4
    print("The new total is", total)
    total /= 2
    print("The new total is", total)

    total = 98.2
    count = 5
    average = total/count
    print("The average is", average)

def data_types():
    print(type(False))
    print(type(1000))
    print(type(100.111))
    print(type("Hello"))
    print(type(True))
    print(type(100/5))
    print(type(100//5))

    print("I'm Sorry\n" * 10)

def Using_built_in_Functions():
    name = input("What's your name? ")
    print("Hello ", name)

    age = int(input("Enter your age: "))
    print("In one year you will be", age + 1)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("The product is", num1 * num2)

def Quotes():
    print("This text includes characters such as '\\' '\"' and \"\'\" \n \t This is a new line that starts with a tab\n \t \t This new line start with two tabs")

    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello There!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

    print("This text spans three lines,\nand includes both single (\'),\nand double quotes (\").")

def indexing_and_slicing():
    surname = "palin"
    initial = surname[2]
    print (initial)

    last = surname[-2]
    print(last)

    middle = surname[1:5]
    print(middle)

    tail = surname[:4]
    print(tail)


    primes = [2,3,5,7,13,17,19,23,31,37,41,43,47]
    First_Four = primes[:4]
    print(First_Four)


    names = ["Tim", "Bill", "Graeme"]
    names[2:0] = ["Mohammed", "Luke"]
    print(names)
#Variable_assigment()
#data_types()
#Using_built_in_Functions()
#Quotes()
indexing_and_slicing()