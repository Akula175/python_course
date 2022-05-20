def define_pos(symb):
    global pos_of_s
    global pos_of_1
    global pos_of_2
    pos_of_s = usr_in.find(symb)
    pos_of_1 = int(usr_in[0:pos_of_s])
    pos_of_2 = int(usr_in[pos_of_s+1:])

def define_weird_pos(symb):
    global pos_of_s
    global pos_of_1
    global pos_of_2
    pos_of_s = usr_in.find(symb)
    pos_of_2 = int(usr_in[pos_of_s+1:])

def addition():
    global last_ans
    print(pos_of_1+pos_of_2)
    last_ans = pos_of_1+pos_of_2

def subtraction():
    global last_ans
    print(pos_of_1-pos_of_2)
    last_ans = pos_of_1-pos_of_2

def divide():
    global last_ans
    print(pos_of_1/pos_of_2)
    last_ans = pos_of_1/pos_of_2

def cars2():
    global last_ans
    print(pos_of_1*pos_of_2)
    last_ans = pos_of_1*pos_of_2

def ans_addition():
    global last_ans
    print(last_ans+pos_of_2)
    last_ans = last_ans+pos_of_2

def ans_subtraction():
    global last_ans
    print(last_ans-pos_of_2)
    last_ans = last_ans-pos_of_2

def ans_divide():
    global last_ans
    print(last_ans/pos_of_2)
    last_ans = last_ans/pos_of_2

def ans_cars2():
    global last_ans
    print(last_ans*pos_of_2)
    last_ans = last_ans*pos_of_2

if __name__ == "__main__":
    while True:
        usr_in = input("Enter calculation: ")
        if not usr_in.find("ans+") == -1:
            define_weird_pos("+")
            ans_addition()
        elif not usr_in.find("ans-") == -1:
            define_weird_pos("-")
            ans_subtraction()
        elif not usr_in.find("ans/") == -1:
            define_weird_pos("/")
            ans_divide()
        elif not usr_in.find("ans*") == -1:
            define_weird_pos("*")
            ans_cars2()
        elif not usr_in.find("+") == -1:
            define_pos("+")
            addition()
        elif not usr_in.find("-") == -1:
            define_pos("-")
            subtraction()
        elif not usr_in.find("*") == -1:
            define_pos("*")
            cars2()
        elif not usr_in.find("/") == -1:
            define_pos("/")
            divide()
        elif usr_in == "ans":
            print(f"Last answer: {last_ans}")
        elif not usr_in.find("ans+") == -1:
            define_weird_pos("+")
            ans_addition()
        elif usr_in == "q":
            print("Bye!")
            break
        else:
            print(f"Invalid input: {usr_in}")
