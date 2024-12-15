adjacency_list = {}
instruction_list = []

with open("input.txt", 'r') as file:
    for line in file:
        if line == "\n":
            break
        num_a, num_b = map(lambda x: int(x), line.strip().split("|"))
        if num_a not in adjacency_list:
            adjacency_list[num_a] = set()
        if num_b not in adjacency_list:
            adjacency_list[num_b] = set()
        adjacency_list[num_a].add(num_b)

    for line in file:
        instruction = list(map(lambda x: int(x), line.strip().split(",")))
        instruction_list.append(instruction)

def middle_number(instruction):
    for i in range(1, len(instruction)):
        compare_number = instruction[i]
        for j in range(i-1, -1, -1):
            num = instruction[j]
            if num in adjacency_list[compare_number]:
                return 0
    mid_index = len(instruction) // 2
    return instruction[mid_index]

sum_mid = 0
for instruction in instruction_list:
    sum_mid += middle_number(instruction)

print(sum_mid)