from Constructor import cuboid1x1x2full

def extractor_new(arr):
    l1 = len(arr)
    l2 = len(arr[0])
    grid = set()
    start = None
    end = None
    for i in range(l1):
        for j in range(l2):
            if arr[i][j] != '0':
                grid.add((i, j))
                if arr[i][j] == 'B':
                    start = ((i, j),)
                if arr[i][j] == 'X':
                    end = ((i, j),)
    return grid, start, end

def blox_solver(ar) -> str:
    #your code goes here. you can do it!
    grid, start, end = extractor_new(ar) # Extract tangible grid
    cuboid = cuboid1x1x2full(start, grid)
    return cuboid.solver(start, end)
