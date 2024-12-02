input_filename = "input.txt"
left_list = []
right_list = []
total_difference = 0

with open(input_filename, "r") as file:
    i = 0
    for line in file:
        left, right = map(lambda x: int(x), line.strip().split("   "))
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    left_value = left_list[i]
    right_value = right_list[i]
    difference = abs(left_value - right_value)
    total_difference += difference

print(total_difference)