import itertools

character_matrix = []

with open("input.txt", 'r') as file:
    for line in file:
        character_matrix.append(line.strip())
    
directions = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
directions.remove((0, 0))
max_rows = len(character_matrix)
max_cols = len(character_matrix[0])
interested_chars = "MAS"
counts = 0

for row_idx in range(max_rows):
    row = character_matrix[row_idx]
    for col_idx in range(max_cols):
        character = row[col_idx]
        if character != "X":
            continue
        for row_incr, col_incr in directions:
            new_row_idx = row_idx
            new_col_idx = col_idx
            character_array = []
            for _ in interested_chars:
                new_row_idx += row_incr
                new_col_idx += col_incr
                if (new_row_idx < 0 or new_row_idx >= max_rows) \
                or (new_col_idx < 0 or new_col_idx >= max_cols):
                    break
                character_array.append(character_matrix[new_row_idx][new_col_idx])
            characters = "".join(character_array)
            if characters == interested_chars:
                counts += 1
            
print(counts)
            
            


