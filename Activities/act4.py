rows = 5
cols = 5
garden_grid = [[None for _ in range(cols)] for _ in range(rows)]

initGardenGrid(rows, cols)

print(f"Garden grid created: {rows}x{cols} 2D list")
for row in garden_grid:
    print(row)