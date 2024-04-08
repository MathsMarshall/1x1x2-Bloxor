import Constructor
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

def is_next_in_bound(cube, direction):
    cube1 = copy.deepcopy(cube)
    cube1.roll(direction)
    return cube1.is_in_bound

def can_roll(cube, direction):
    if cube.path == '':
        return True
    elif (cube.path[-1] == 'U') and (direction == 'D'):
        return False
    elif (cube.path[-1] == 'D') and (direction == 'U'):
        return False
    elif (cube.path[-1] == 'L') and (direction == 'R'):
        return False
    elif (cube.path[-1] == 'R') and (direction == 'L'):
        return False
    else:
        return True

def go(cube, direction):
    return is_next_in_bound(cube, direction) and can_roll(cube, direction)
