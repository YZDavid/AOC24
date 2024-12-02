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
    for i in range(1, len(report)):
        if is_ascending:
            difference = report[i] - report[i - 1]
        else:
            difference = report[i - 1] - report[i]
        if difference <= 0 or difference > 3:
            return 0
    return 1

with open(input_filename, "r") as file:
    for line in file:
        report = list(map(lambda x: int(x), line.strip().split(" ")))
        safe_count += is_safe(report)

print(safe_count)
