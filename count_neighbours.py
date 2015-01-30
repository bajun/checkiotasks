def count_neighbours(grid, row, col):
    counter = 0
    numrows = len(grid)
    numcols = len(grid[0])
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if ([i,j] != [row,col]) and i>=0 and j>=0 and i<=numrows-1 and j<=numcols-1: 
                if ((grid[i][j]==1)):
                    counter+=1
    return counter