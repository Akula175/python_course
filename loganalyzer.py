# Tobias_Gustafsson_tobias.gustafsson@edu.edugrade.se

# Log reader
# Input: loganalyzer.py filepath action
# Possible actions: statistics, error, notice

#statistics:
#errors 340
#notice 450

#error
#date message

#notice
#date message

import sys

file_path = sys.argv[1]

def arg_checker():
    if sys.argv[2] == "statistics":
        print(file_path + " statistics")
    elif sys.argv[2] == "error":
        print(file_path + " error")
    elif sys.argv[2] == "notice":
        print(file_path + " notice")
    else:
        print("Invalid arguments")





if __name__ == "__main__":
    arg_checker()
