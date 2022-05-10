print("This calculator accepts input in the following format\nnum+*-/num")
print("You can also type ans to see the last result")
print("Type q to quit")
while True:
    text_raw = input("Please enter calculation: ")


    if not text_raw.find("+") == -1:
        #print("Found +")

        pos_of_S = text_raw.find("+")
        #print(pos_of_L)

        first_num = int(text_raw[0:pos_of_S])
        #print(first_num)

        second_num = int(text_raw[pos_of_S+1:])
        #print(second_num)

        print("Result: ", first_num+second_num)
        last_ans = (first_num+second_num)

    elif not text_raw.find("/") == -1:
        #print("Found /")

        pos_of_S = text_raw.find("/")
        #print(pos_of_L)

        first_num = int(text_raw[0:pos_of_S])
        #print(first_num)

        second_num = int(text_raw[pos_of_S+1:])
        #print(second_num)

        print("Result: ", first_num/second_num)
        last_ans = (first_num/second_num)

    elif not text_raw.find("-") == -1:
        #print("Found -")

        pos_of_S = text_raw.find("-")
        #print(pos_of_L)

        first_num = int(text_raw[0:pos_of_S])
        #print(first_num)

        second_num = int(text_raw[pos_of_S+1:])
        #print(second_num)

        print("Result: ", first_num-second_num)
        last_ans = (first_num-second_num)

    elif not text_raw.find("*") == -1:
        #print("Found *")

        pos_of_S = text_raw.find("*")
        #print(pos_of_L)

        first_num = int(text_raw[0:pos_of_S])
        #print(first_num)

        second_num = int(text_raw[pos_of_S+1:])
        #print(second_num)

        print("Result: ", first_num*second_num)
        last_ans = (first_num*second_num)

    elif text_raw == "q":
        print("Bye!")
        break

    elif text_raw == "ans":
        print("Result of last: ", last_ans)
    else:
        print("Invalid Input: " + text_raw)
