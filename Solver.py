# solver1() is designed to solve from the start coordinate 
# and solver2() is designed to solve from the end coordinate
import Constructor
import Foundation

def solver1(my_dict, my_dict1, grid, end):
    '''Updates set of possible paths. paths is a 
    list of the possible .path attributes. coordinates is 
    a list of coordinates occupied. path in paths are the keys
    for coordinate in coordinates for dictionary my_dict,
    my_dict1 has corresponding keys with my_dict, but value is
    current coordinate as tuple'''
    my_dict_ = {}
    my_dict1_ = {}
    check = {}
    checkset = set()
    Directions = ['U', 'D', 'L', 'R']
    for path, coordinate in my_dict1.items(): # Here coordinate is a tuple of tuples
        coordinates = my_dict[path]
        for direction in Directions:
            a = cuboid1x1x2(coordinate, grid)
            a.path = path
            if go(a, direction):
                a.roll(direction) # Perform roll
                if a.coordinate not in my_dict[path]: 
                    ss = copy.deepcopy(my_dict[path])
                    ss.add(a.coordinate)
                    my_dict_[a.path] = ss # Update list of coordinates occupied for paths
                    my_dict1_[a.path] = a.coordinate # Update current coordinate occupied with respect to path
                    check[a.coordinate] = a.path #  Inverse dictionary for my_dict1_
                    checkset.add(a.coordinate) # Set of coordinates occupied
    return my_dict_, my_dict1_, check, checkset

def solver2(my_dict, my_dict1, grid, end):
    '''Updates set of possible recalls. recalls is a 
    list of the possible .recall attributes. coordinates is 
    a list of coordinates occupied. recall in recalls are the keys
    for coordinate in coordinates for dictionary my_dict,
    my_dict1 has corresponding keys with my_dict, but value is
    current coordinate as tuple'''
    my_dict_ = {}
    my_dict1_ = {}
    check = {}
    checkset = set()
    Directions = ['U', 'D', 'L', 'R']
    for recall, coordinate in my_dict1.items(): # Here coordinate is a tuple of tuples
        coordinates = my_dict[recall]
        for direction in Directions:
            a = cuboid1x1x2(coordinate, grid)
            a.recall = recall
            if go(a, direction):
                a.roll(direction) # Perform roll
                if a.coordinate not in my_dict[recall]: 
                    ss = copy.deepcopy(my_dict[recall])
                    ss.add(a.coordinate)
                    my_dict_[a.recall] = ss # Update list of coordinates occupied for recalls
                    my_dict1_[a.recall] = a.coordinate # Update current coordinate occupied with respect to recall
                    check[a.coordinate] = a.recall # Inverse dictionary for my_dict1_
                    checkset.add(a.coordinate) # Set of coordinates occupied
    return my_dict_, my_dict1_, check, checkset

def blox_solver(ar):
    #your code goes here. you can do it!
    tup_ar = tuple(ar)
    if tup_ar in Aar:
        return ar_dict[tup_ar]
    print(ar)
    grid, start, end = extractor_new(ar) # Extract tangible grid
    cuboid = cuboid1x1x2(start, grid) # Create cuboid
    my_dict = {'': {tuple(start)}}
    my_dict1 = {'': tuple(start)}
    my_dict_ = {'': {tuple(end)}}
    my_dict1_ = {'': tuple(end)}
    my_dict, my_dict1, check, checkset = solver1(my_dict, my_dict1, grid, end)
    while True:
        my_dict_, my_dict1_, check_, checkset_ = solver2(my_dict_, my_dict1_, grid, start)
        if checkset & checkset_:
            s = list(checkset & checkset_)[0]
            s1 = check[s] + check_[s]
            return s1
        my_dict, my_dict1, check, checkset = solver1(my_dict, my_dict1, grid, end)
        if checkset & checkset_:
            s = list(checkset & checkset_)[0]
            s1 = check[s] + check_[s]
            return s1
