def boolen_expressions():
    print(10<100)
    print(100!=100)
    print(50>=50)

    age = int(input("Enter your age: "))
    print("It is", age<18, "that you are younger than", 18)
    print("It is", age<21, "that you are younger than", 21)
    print("It is", age<31, "that you are younger than", 31)

    print("")
    print("a" < "b")
    print("b" < "a")
    print("John" < "Terry")
    print("john" < "Terry")
    print("")

    print(5 < 10.2)

def Logic_operators_within_expressions():
    age = 30
    print(age >= 18 and age <= 65)
    print(age < 18 or age > 65)
    print(not age > 18)
    print("")

    print((age >= 18 and age <= 65) and (not age == 30))
    print("")

    weight = int(input("Enter your weight: "))
    height = int(input("Enter your height: "))
    print(100 < weight and weight <200)
    print(height > 131 and height < 160)
    print("")

    names = ["John", "Terry", "Michael", "Eric", "Terry", "Graham"]
    checking = "Eric" in names and "Luke" not in names
    print(checking)

def If_Else_Elif_Statement():
    age = int(input("Enter your age: "))
    if age >= 18 and age <= 30:
        print("You are still a baby")
    else:
        print("You are old")

    if age >= 100:
        print ("You Old")
    elif age >= 80:
        print ("You Kinda Old")
    elif age >= 40:
        print ("You not Old")
    else:
        print ("You are a baby")

    name = input("Enter your name: ")
    if str(name) in name:
        print("Your name is", name)
    else:
        print("Name not entered")

    print("You are an adult" if age>=18 else "You are a teenager")

def While_loop():
    names = ["John", "Terry", "Michael", "Luke"]
    i = 0
    while i < 4:
        print(names[i])
        i +=1

    for n in range(6):
        if n == 0:
            n += 1
        n *= 2
        print(n, "to the power of", n, "is", n**n)

#boolen_expressions()
#Logic_operators_within_expressions()
#If_Else_Elif_Statement()
While_loop()