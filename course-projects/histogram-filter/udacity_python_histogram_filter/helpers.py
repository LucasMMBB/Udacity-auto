def blur(grid, blurring):
	height = len(grid)
	width = len(grid[0])

	center_prop = 1.0 - blurring
	corner_prop = blurring / 12.0
	adjacent_prop = blurring / 6.0

	window = [
	    [corner_prop, adjacent_prop, corner_prop],
	    [adjacent_prop, center_prop, adjacent_prop],
	    [corner_prop, adjacent_prop, corner_prop]
	]

	new = [[0.0 for i in range(width)] for j in range(height)]

	for i in range(height):
		for j in range(width):
			grid_val = grid[i][j]
			for dx in range(-1, 2):
				for dy in range(-1, 2):
					mult = window[dx+1][dy+1]
					new_i = (i + dx) % height
					new_j = (j + dy) % width
					print new_i
					print new_j
					print "---------"
					new[new_i][new_j] += mult*grid_val
	return new

grid = [[1,2],[2,3]]
blurring = 0.1

print blur(grid, blurring)