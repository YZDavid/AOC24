adjacency_list = {}
visited = {}
instruction_list = []
topo_stack = []
topo_sorted = []

with open("input.txt", 'r') as file:
    for line in file:
        if line == "\n":
            break
        num_a, num_b = map(lambda x: int(x), line.strip().split("|"))
        if num_a not in adjacency_list:
            adjacency_list[num_a] = []
            visited[num_a] = 0
        if num_b not in adjacency_list:
            adjacency_list[num_b] = []
            visited[num_b] = 0
        adjacency_list[num_a].append(num_b)

    for line in file:
        instruction = list(map(lambda x: int(x), line.strip().split(",")))
        instruction_list.append(instruction)

def dfs(node):
    print(f"visiting {node}")
    visited[node] = 1
    neighbours = adjacency_list[node]
    for neighbour in neighbours:
        if visited[neighbour] == 0:
            dfs(neighbour)
    print(f"appending {node}")
    topo_stack.append(node)

for num in adjacency_list:
    if visited[num] == 1:
        continue
    dfs(num)

while topo_stack:
    topo_sorted.append(topo_stack.pop())

nums_order = {}
for i, num in enumerate(topo_sorted):
    nums_order[num] = i

mid_num_sum = 0

for instruction in instruction_list:
    valid_instruction = True
    for i in range(len(instruction) - 1):
        curr_number = instruction[i]
        next_number = instruction[i + 1]
        if nums_order[next_number] < nums_order[curr_number]:
            valid_instruction = False
            break
    if valid_instruction:
        mid_idx = int((len(instruction) - 1) / 2)
        mid_num_sum += instruction[mid_idx]
