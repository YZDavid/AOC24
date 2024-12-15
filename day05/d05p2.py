adjacency_list = {}
instruction_list = []

with open("input.txt", 'r') as file:
    for line in file:
        if line == "\n":
            break
        num_a, num_b = map(lambda x: int(x), line.strip().split("|"))
        if num_a not in adjacency_list:
            adjacency_list[num_a] = []
        if num_b not in adjacency_list:
            adjacency_list[num_b] = []
        adjacency_list[num_a].append(num_b)

    for line in file:
        instruction = list(map(lambda x: int(x), line.strip().split(",")))
        instruction_list.append(instruction)

def toposort(nums):
    visited = {}
    topo_stack = []
    topo_sorted = []
    for num in nums:
        visited[num] = 0

    def dfs(node, valid_nums):
        visited[node] = 1
        neighbours = adjacency_list[node]
        for neighbour in neighbours:
            if neighbour in valid_nums and visited[neighbour] == 0:
                dfs(neighbour, valid_nums)
        topo_stack.append(node)
    
    for num in nums:
        if visited[num] == 1:
            continue
        dfs(num, nums)

    while topo_stack:
        topo_sorted.append(topo_stack.pop())

    return topo_sorted

def middle_number(instruction):
    for i in range(1, len(instruction)):
        compare_number = instruction[i]
        for j in range(i-1, -1, -1):
            num = instruction[j]
            if num in adjacency_list[compare_number]:
                return 0
    mid_index = len(instruction) // 2
    return instruction[mid_index]

sum_mid_num = 0

for instruction in instruction_list:
    if middle_number(instruction) != 0:
        continue
    mid_idx = len(instruction) // 2
    sum_mid_num += toposort(instruction)[mid_idx]

print(sum_mid_num)



