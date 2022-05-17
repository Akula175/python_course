def add_func():
    global last_ans
    pos_of_O = usr_in.find("+")
    first_num = int(usr_in[0:pos_of_O])
    second_num = int(usr_in[pos_of_O+1:])

    print("Result: ", first_num + second_num)
    last_ans = (first_num + second_num)

def sub_func():
    global last_ans
    pos_of_O = usr_in.find("-")
    first_num = int(usr_in[0:pos_of_O])
    second_num = int(usr_in[pos_of_O+1:])

    print("Result: ", first_num-second_num)
    last_ans = (first_num-second_num)

def divide_func():
    global last_ans
    pos_of_O = usr_in.find("/")
    first_num = int(usr_in[0:pos_of_O])
    second_num = int(usr_in[pos_of_O+1:])

    print("Result: ", first_num/second_num)
    last_ans = (first_num/second_num)

def multi_func():
    global last_ans
    pos_of_O = usr_in.find("*")
    first_num = int(usr_in[0:pos_of_O])
    second_num = int(usr_in[pos_of_O+1:])

    print("Result: ", first_num*second_num)
    last_ans = (first_num*second_num)

def factor_func():
    global last_ans
    pos_of_O = usr_in.find("!")
    first_num = int(usr_in[0:pos_of_O])
    res = 1

    for i in range(1, first_num+1):
        res = res * i
    print("Result: ", res)
    last_ans = (res*i)



print("This calculator accepts input in the following format\nnum+*-/num")
print("You can also type ans to see the last result")
print("Type q to quit")
while True:
    usr_in = input("Please enter calculation: ")


    if usr_in.find("+") == True:
        add_func()

    elif usr_in.find("/") == True:
        divide_func()

    elif usr_in.find("-") == True:
        sub_func()

    elif usr_in.find("*") == True:
        multi_func()

    elif usr_in.find("!") == True:
        factor_func()

    elif usr_in == "q":
        print("Bye!")
        break

    elif usr_in == "ans":
        print("Result of last: ", last_ans)

    elif "ans" in usr_in:  #Find ["+", osv.]
        if "+" in usr_in:
            pos_of_O = usr_in.find("+")
            second_num = int(usr_in[pos_of_O+1:])
            print("Result: ", last_ans + second_num)
            last_ans = (last_ans + second_num)

        elif "-" in usr_in:
            pos_of_O = usr_in.find("-")
            second_num = int(usr_in[pos_of_O+1:])
            print("Result: ", last_ans - second_num)
            last_ans = (last_ans - second_num)

        elif "/" in usr_in:
            pos_of_O = usr_in.find("/")
            second_num = int(usr_in[pos_of_O+1:])
            print("Result: ", last_ans / second_num)
            last_ans = (last_ans / second_num)

        elif "*" in usr_in:
            pos_of_O = usr_in.find("*")
            second_num = int(usr_in[pos_of_O+1:])
            print("Result: ", last_ans * second_num)
            last_ans = (last_ans * second_num)

        else:
            print("Invalid")


    else:
        print("Invalid Input: " + usr_in)
