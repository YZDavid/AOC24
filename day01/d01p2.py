input_filename = "input.txt"
left_list = []
right_list = []
similarity_score = 0

with open(input_filename, "r") as file:
    i = 0
    for line in file:
        left, right = map(lambda x: int(x), line.strip().split("   "))
        left_list.append(left)
        right_list.append(right)

right_num_count = dict()
for num in right_list:
    right_num_count[num] = right_num_count.get(num, 0) + 1

for num in left_list:
    score = num * right_num_count.get(num, 0)
    similarity_score += score

print(similarity_score)