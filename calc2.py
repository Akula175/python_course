def add_func():
    global last_ans
    global number_1
    global number_2

    usr_in = input("Enter calculation: ")
    pos_of_O = usr_in.find("+")
    number_1 = int(usr_in[0:pos_of_O])
    number_2 = int(usr_in[pos_of_O+1:])

    print(number_1+number_2)
    last_ans = number_1+number_2

def sub_func():
    global last_ans
    global number_1
    global number_2
    usr_in = input("Enter calculation: ")
    pos_of_O = usr_in.find("-")
    number_1 = int(usr_in[0:pos_of_O])
    number_2 = int(usr_in[pos_of_O+1:])

    print(number_1-number_2)
    last_ans = number_1-number_2

def multi_func():
    global last_ans
    global number_1
    global number_2

    usr_in = input("Enter calculation: ")
    pos_of_O = usr_in.find("*")
    number_1 = int(usr_in[0:pos_of_O])
    number_2 = int(usr_in[pos_of_O+1:])

    print(number_1*number_2)
    last_ans = number_1*number_2

def divide_func():
    global last_ans
    global number_1
    global number_2

    usr_in = input("Enter calculation: ")
    pos_of_O = usr_in.find("/")
    number_1 = int(usr_in[0:pos_of_O])
    number_2 = int(usr_in[pos_of_O+1:])

    print(number_1/number_2)
    last_ans = number_1/number_2

def lans_func():
    global last_ans
    global number_1
    global number_2

    usr_in = input("Enter calculation: ")
    pos_of_O = usr_in.find("+")
    number_1 = last_ans
    number_2 = int(usr_in[pos_of_O+1:])

    print(number_1+number_2)
    last_ans = number_1+number_2


print("Welcome to calculator, please enter which action to perform")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
print("q to Quit")

while True:
    operator = input("Enter action to perform: ")

    if operator == "+":
        add_func()
    elif operator == "-":
        sub_func()
    elif operator == "*":
        multi_func()
    elif operator == "/":
        divide_func()
    elif operator == "Lans":
        lans_func()
    elif operator == "ans":
        print("Result of last: ", last_ans)
    elif operator == "q":
        print("Bye!")
        break
    else:
        print("Invalid Input: " + operator)
