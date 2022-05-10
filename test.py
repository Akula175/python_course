#!/usr/bin/env/python3

first_name = "Bob"

last_name = "Lakul"

age = 46

active = True

salary = 35000.60

print(first_name)
print(type(first_name))

print(age)
print(type(age))

print(active)
print(type(active))

print(salary)
print(type(salary))



#hobby = input("What is your Hobby?: ")
#print("Your hobby is: " + hobby)

print("Hello\nNewline") # \n inserts newline

print("Hello\tTabbing") # \t inserts tab

print(len(first_name)) # len() Shows length of str



x = " Test "
print(x)
print(len(x))

x_less = x.strip()
print(x_less)
print(len(x_less))






# Loops and if statements

y = 3
x = 6

if x > y:
    print(x, "is bigger than", y)
else:
    print(y, "is bigger than", x)


# x = input("Enter value for X: ")
# y = input("Enter value for Y: ")
#
# if x > y:
#     print(x, "is bigger than", y)
# elif x == y:
#     print(x, "and", y, "are the same" )
# else:
#     print(y, "is bigger than", x)



# print("1 Add user")
# print("2 Delete user")
# command = input("Enter command:")
#
# if command == "1":
#     print("Adding user")
# elif command == "2":
#     print("Deleting user")
# else:
#     print("Unknown command: " + command)





# count = 0
# while count < 10:
#     print(count)
#     count += 1




# print("Available commands")
# print("1 Add user")
# print("2 Delete user")
# print("3 Quit")
# while True:
#     command = input("Enter command: ")
#     if command == "1":
#         print("Adding user")
#     elif command == "2":
#         print("Deleting user")
#     elif command == "3":
#         print("Bye!")
#         break
#     else:
#         print("Unknown command: " + command)


#for i in range(10):
#    print(i)



# For calc

text_raw = "60*2"

if not text_raw.find("+") == -1:
    print("Found +")

    pos_of_L = text_raw.find("+")
    print(pos_of_L)

    first_num = text_raw[0:pos_of_L]
    print(first_num)
    first_num_int = int(first_num)

    second_num = text_raw[pos_of_L+1:]
    print(second_num)
    sec_num_int = int(second_num)

    print(first_num_int+sec_num_int)

elif not text_raw.find("/") == -1:
    print("Found /")

    pos_of_L = text_raw.find("/")
    print(pos_of_L)

    first_num = text_raw[0:pos_of_L]
    print(first_num)
    first_num_int = int(first_num)

    second_num = text_raw[pos_of_L+1:]
    print(second_num)
    sec_num_int = int(second_num)

    print(first_num_int/sec_num_int)

elif not text_raw.find("-") == -1:
    print("Found -")

    pos_of_L = text_raw.find("-")
    print(pos_of_L)

    first_num = text_raw[0:pos_of_L]
    print(first_num)
    first_num_int = int(first_num)

    second_num = text_raw[pos_of_L+1:]
    print(second_num)
    sec_num_int = int(second_num)

    print(first_num_int-sec_num_int)

elif not text_raw.find("*") == -1:
    print("Found *")

    pos_of_L = text_raw.find("*")
    print(pos_of_L)

    first_num = text_raw[0:pos_of_L]
    print(first_num)
    first_num_int = int(first_num)

    second_num = text_raw[pos_of_L+1:]
    print(second_num)
    sec_num_int = int(second_num)

    print(first_num_int*sec_num_int)
else:
    print("Found none")

# test_text_raw = "22"
# test_text = int(test_text_raw)
# print(test_text)
# print(test_text+1)


# pos_of_L = text.find("H")
# print(pos_of_L)
#
# date_str = text[0:pos_of_L]
# print(date_str)
#
# time_str = text[pos_of_L+1:]
# print(time_str)
