# Tobias_Gustafsson_tobias.gustafsson@edu.edugrade.se

# Log reader
# Input: loganalyzer.py filepath action
# Possible actions: statistics, error, notice

#statistics:
#errors 340
#notice 450
#DONE

#error
#date message

#notice
#date message

import sys

file_path = sys.argv[1]

def arg_checker():
    if sys.argv[2] == "statistics":
        stats()
    elif sys.argv[2] == "error":
        print(file_path + " error")
    elif sys.argv[2] == "notice":
        print(file_path + " notice")
    else:
        print("Invalid arguments")

def stats():
    notice_count = 0
    error_count = 0
    with open(file_path) as f:
        for line in f:
            if "error" in line:
                error_count +=1
            if "notice" in line:
                notice_count +=1
    print("errors", error_count)
    print("notice", notice_count)


def log_print():
    count = 0
    with open(file_path) as f:
        for line in f:
            if "error" in line:
                print(line)
                count +=1
                print(count)




if __name__ == "__main__":
    arg_checker()
