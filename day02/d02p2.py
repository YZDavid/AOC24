input_filename = "input.txt"
safe_count = 0

def is_safe(report):
    difference = report[1] - report[0]
    if not difference:
        return 0
    if difference > 0:
        is_ascending = True
    else:
        is_ascending = False

    def check_number(first_number, second_number, ascending_bool):
        if ascending_bool:
            difference = second_number - first_number
        else:
            difference = first_number - second_number
        if difference <= 0 or difference > 3:
            return False
        return True

    for i in range(1, len(report)):
        first_num = report[i - 1]
        second_num = report[i]
        if not check_number(first_num, second_num, is_ascending):
            if i == len(report) - 1:
                return 1
            if not check_number(first_num, report[i + 1], is_ascending):
                return 0
                
    return 1

with open(input_filename, "r") as file:
    for line in file:
        report = list(map(lambda x: int(x), line.strip().split(" ")))
        safe_count += is_safe(report)

print(safe_count)
