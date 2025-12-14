a = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [1,0,1,0,0],
    [0,1,1,0,0],
    [0,0,0,0,0],
]

HEIGHT = len(a)
WIDTH = len(a[0])

b = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

alive_neighbours = 0

for i, x in enumerate(a):
    for j, y in enumerate(x):

        # the holy wall of if-statements
        if (i-1 >= 0) and (i-1 < HEIGHT) and (j-1 >= 0) and (j-1 < WIDTH) and a[i-1][j-1] == 1: alive_neighbours += 1 # up left
        if (i-1 >= 0) and (i-1 < HEIGHT)                                  and a[i-1][j]   == 1: alive_neighbours += 1 # up
        if (i-1 >= 0) and (i-1 < HEIGHT) and (j+1 >= 0) and (j+1 < WIDTH) and a[i-1][j+1] == 1: alive_neighbours += 1 # up right
        
        if                                   (j-1 >= 0) and (j-1 < WIDTH) and a[i][j-1]   == 1: alive_neighbours += 1 # left
        if                                   (j+1 >= 0) and (j+1 < WIDTH) and a[i][j+1]   == 1: alive_neighbours += 1 # right
        
        if (i+1 >= 0) and (i+1 < HEIGHT) and (j-1 >= 0) and (j-1 < WIDTH) and a[i+1][j-1] == 1: alive_neighbours += 1 # down left
        if (i+1 >= 0) and (i+1 < HEIGHT)                                  and a[i+1][j]   == 1: alive_neighbours += 1 # down
        if (i+1 >= 0) and (i+1 < HEIGHT) and (j+1 >= 0) and (j+1 < WIDTH) and a[i+1][j+1] == 1: alive_neighbours += 1 # down right

        # Any live cell...
        if a[i][j] == 1:
            # with fewer than two live neighbours dies, as if by underpopulation.
            if alive_neighbours < 2:
                b[i][j] = 0

            # with two or three live neighbours lives on to the next generation.
            elif alive_neighbours in [2,3]:
                b[i][j] = 1

            # with more than three live neighbours dies, as if by overpopulation.
            elif alive_neighbours > 3:
                b[i][j] = 0

        # Any dead cell...
        if a[i][j] == 0:
            # with exactly three live neighbours becomes a live cell, as if by reproduction.
            if alive_neighbours == 3:
                b[i][j] = 1

        # neighbours reset
        alive_neighbours = 0

for row in b:
    print(row)