# Tobias_Gustafsson_tobias.gustafsson@edu.edugrade.se
import sys
file_path = sys.argv[1]

def arg_checker():
    if sys.argv[2] == "statistics":
        stats()
    elif sys.argv[2] == "error":
        line_print("error", 35)
    elif sys.argv[2] == "notice":
        line_print("notice", 36)
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


def line_print(t, n):
    with open(file_path) as f:
        for line in f:
            if t in line:
                date = (line[:26])
                type = (line[27:34])
                msg = (line[n:])
                print(date, msg)


if __name__ == "__main__":
    arg_checker()
