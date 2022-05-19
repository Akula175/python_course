# Tobias_Gustafsson_tobias.gustafsson@edu.edugrade.se
import sys
file_path = sys.argv[1]

def arg_check():
    if sys.argv[2] == "statistics":
        stats()
    elif sys.argv[2] == "error":
        line_print("error", 35)
    elif sys.argv[2] == "notice":
        line_print("notice", 36)
    else:
        print("ERROR: Invalid arguments")

def stats():
    notice_count = 0
    error_count = 0
    try:
        with open(file_path) as f:
            for line in f:
                if "error" in line:
                    error_count +=1
                if "notice" in line:
                    notice_count +=1
        print("errors", error_count)
        print("notice", notice_count)
    except FileNotFoundError:
        print("ERROR: File " + file_path + " not found")
        return False
    return True

def line_print(t, n):
    try:
        with open(file_path) as f:
            for line in f:
                if t in line:
                    date = (line[:26])
                    type = (line[27:35])
                    msg = (line[n:])
                    print(date + " " + msg)
    except FileNotFoundError:
        print("ERROR: File " + file_path + " not found")
        return False
    return True

if __name__ == "__main__":
    arg_check()
