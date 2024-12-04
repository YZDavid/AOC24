character_matrix = []

with open("input.txt", 'r') as file:
    for line in file:
        character_matrix.append(line.strip())
    
directions = [(-1, -1, 1, 1), (1, -1, -1, 1)]
max_rows = len(character_matrix)
max_cols = len(character_matrix[0])
counts = 0

for row_idx in range(max_rows):
    row = character_matrix[row_idx]
    for col_idx in range(max_cols):
        character = row[col_idx]
        if character != "A":
            continue
        criteria = 0
        for xi1, yi1, xi2, yi2 in directions:
            x1 = row_idx + xi1
            y1 = col_idx + yi1
            x2 = row_idx + xi2
            y2 = col_idx + yi2
            if (x1 < 0 or x1 >= max_rows) \
            or (x2 < 0 or x2 >= max_rows) \
            or (y1 < 0 or y1 >= max_cols) \
            or (y2 < 0 or y2 >= max_cols):
                break
            d1 = character_matrix[x1][y1]
            d2 = character_matrix[x2][y2]
            if d1 in ("M", "S") and d2 in ("M", "S") and d1 != d2:
                criteria += 1
        if criteria == 2:
            counts += 1
            
print(counts)
            
            


