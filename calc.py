print("This calculator accepts input in the following format\nnum+*-/num")
print("You can also type ans to see the last result")
print("Type q to quit")
while True:
    text_raw = input("Please enter calculation: ")


    if not text_raw.find("+") == -1:
        #print("Found +")

        pos_of_L = text_raw.find("+")
        #print(pos_of_L)

        first_num = text_raw[0:pos_of_L]
        #print(first_num)
        first_num_int = int(first_num)

        second_num = text_raw[pos_of_L+1:]
        #print(second_num)
        sec_num_int = int(second_num)

        print("Result: ", first_num_int+sec_num_int)
        last_ans = (first_num_int+sec_num_int)

    elif not text_raw.find("/") == -1:
        #print("Found /")

        pos_of_L = text_raw.find("/")
        #print(pos_of_L)

        first_num = text_raw[0:pos_of_L]
        #print(first_num)
        first_num_int = int(first_num)

        second_num = text_raw[pos_of_L+1:]
        #print(second_num)
        sec_num_int = int(second_num)

        print("Result: ", first_num_int/sec_num_int)
        last_ans = (first_num_int/sec_num_int)

    elif not text_raw.find("-") == -1:
        #print("Found -")

        pos_of_L = text_raw.find("-")
        #print(pos_of_L)

        first_num = text_raw[0:pos_of_L]
        #print(first_num)
        first_num_int = int(first_num)

        second_num = text_raw[pos_of_L+1:]
        #print(second_num)
        sec_num_int = int(second_num)

        print("Result: ", first_num_int-sec_num_int)
        last_ans = (first_num_int-sec_num_int)

    elif not text_raw.find("*") == -1:
        #print("Found *")

        pos_of_L = text_raw.find("*")
        #print(pos_of_L)

        first_num = text_raw[0:pos_of_L]
        #print(first_num)
        first_num_int = int(first_num)

        second_num = text_raw[pos_of_L+1:]
        #print(second_num)
        sec_num_int = int(second_num)

        print("Result: ", first_num_int*sec_num_int)
        last_ans = (first_num_int*sec_num_int)

    elif text_raw == "q":
        print("Bye!")
        break

    elif text_raw == "ans":
        print("Result of last: ", last_ans)
    else:
        print("Invalid Input: " + text_raw)
