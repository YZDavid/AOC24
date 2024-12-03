instructions = []
enabled = True

with open("input.txt", "r") as file:
    for line in file:
        for i in range(len(line)):
            instruction_keyword = line[i:i+4]
            enable_keyword = line[i:i+4]
            disable_keyword = line[i:i+7]
            if instruction_keyword == "mul(" and enabled:
                instruction = line[i:i+12]
                instructions.append(instruction)
            if enable_keyword == "do()":
                enabled = True
            if disable_keyword == "don't()":
                enabled = False

def multiply_instruction(instruction):
    closing_parenthesis_idx = instruction.find(")")
    if closing_parenthesis_idx == -1:
        return 0
    numeric_segment = instruction[4:closing_parenthesis_idx]
    try:
        num1, num2 = numeric_segment.split(",")
    except:
        return 0
    if not num1.isnumeric() or not num2.isnumeric():
        return 0
    return int(num1) * int(num2)

total = sum(map(lambda x: multiply_instruction(x), instructions))
print(total)