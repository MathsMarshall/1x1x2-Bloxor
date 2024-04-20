import copy
class cuboid1x1x2full():
    def __init__(self, coordinate: tuple[tuple], grid: str):
        self.coordinate = coordinate # tuple of tuples
        self.path = '' # string of direction
        self.recall = '' # string of reverse direction
        self.grid = grid # set of tuples
    @property
    def state(self) -> str:
        c = self.coordinate
        if len(c) == 1:
            return '1x1'
        elif c[0][1] == c[1][1]:
            return '2x1'
        else: # c[0][0] == c[1][0]
            return '1x2'
    @property
    def is_in_bound(self) -> bool: # grid is a set of tuples
        return (set(self.coordinate).issubset(self.grid))
    
    @staticmethod
    def opposite(direction: str) -> str:
        if (direction == 'U'):
            return 'D'
        elif (direction == 'D'):
            return 'U'
        elif (direction == 'L'):
            return 'R'
        else:# (direction == 'R'):
            return 'L'
    
    def not_reverse(self, direction: str) -> bool:
        if self.path == '':
            return True
        elif (self.path[-1] == 'U') and (direction == 'D'):
            return False
        elif (self.path[-1] == 'D') and (direction == 'U'):
            return False
        elif (self.path[-1] == 'L') and (direction == 'R'):
            return False
        elif (self.path[-1] == 'R') and (direction == 'L'):
            return False
        else:
            return True
    
    def is_next_in_bound(self, direction: str) -> bool:
        cube = copy.copy(self)
        cube.roll(direction)
        return cube.is_in_bound

    def go(self, direction: str) -> bool:
        return self.is_next_in_bound(direction) and self.not_reverse(direction)


    def forward(self, my_dict: dict, my_dict1: dict, end: tuple[tuple]) -> tuple[dict, dict, dict, set]:
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
                a = cuboid1x1x2full(coordinate, self.grid)
                a.path = path
                if a.go(direction):
                    a.roll(direction) # Perform roll
                    if a.coordinate not in my_dict[path]: 
                        ss = copy.deepcopy(my_dict[path])
                        ss.add(a.coordinate)
                        my_dict_[a.path] = ss # Update list of coordinates occupied for paths
                        my_dict1_[a.path] = a.coordinate # Update current coordinate occupied with respect to path
                        check[a.coordinate] = a.path #  Inverse dictionary for my_dict1_
                        checkset.add(a.coordinate) # Set of coordinates occupied
        return my_dict_, my_dict1_, check, checkset

    def backward(self, my_dict: dict, my_dict1: dict, start: tuple[tuple]) -> tuple[dict, dict, dict, set]:
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
                a = cuboid1x1x2full(coordinate, self.grid)
                a.recall = recall
                if a.go(direction):
                    a.roll(direction) # Perform roll
                    if a.coordinate not in my_dict[recall]: 
                        ss = copy.deepcopy(my_dict[recall])
                        ss.add(a.coordinate)
                        my_dict_[a.recall] = ss # Update list of coordinates occupied for recalls
                        my_dict1_[a.recall] = a.coordinate # Update current coordinate occupied with respect to recall
                        check[a.coordinate] = a.recall # Inverse dictionary for my_dict1_
                        checkset.add(a.coordinate) # Set of coordinates occupied
        return my_dict_, my_dict1_, check, checkset

    def solver(self, start: tuple[tuple], end: tuple[tuple]) -> str:
        cuboid = cuboid1x1x2full(start, self.grid) # Create cuboid
        my_dict = {'': {tuple(start)}}
        my_dict1 = {'': tuple(start)}
        my_dict_ = {'': {tuple(end)}}
        my_dict1_ = {'': tuple(end)}
        my_dict, my_dict1, check, checkset = self.forward(my_dict, my_dict1, end)
        while True:
            my_dict_, my_dict1_, check_, checkset_ = self.backward(my_dict_, my_dict1_, start)
            if checkset & checkset_:
                s = list(checkset & checkset_)[0]
                s1 = check[s] + check_[s]
                return s1
            my_dict, my_dict1, check, checkset = self.forward(my_dict, my_dict1, end)
            if checkset & checkset_:
                s = list(checkset & checkset_)[0]
                s1 = check[s] + check_[s]
                return s1
    
    def roll(self, direction: str) -> None: # direction is a string from U, D, L, R
        self.path = self.path + direction
        self.recall = self.opposite(direction) + self.recall
        c = self.coordinate # tuple
        a = c[0][0]
        b = c[0][1]
        # c is of the form ((a, b),) or ((a0, b0), (a1, b1))
        if self.state == '1x1':
            if direction == 'U':
                self.coordinate = ((a-2, b), (a-1, b))
            elif direction == 'D':
                self.coordinate = ((a+1, b), (a+2, b))
            elif direction == 'L':
                self.coordinate = ((a, b-2), (a, b-1))
            else: # direction == 'R'
                self.coordinate = ((a, b+1), (a, b+2))
        elif self.state == '2x1':
            if direction == 'U':
                self.coordinate = ((min(a, c[1][0])-1, b),)
            elif direction == 'D':
                self.coordinate = ((max(a, c[1][0])+1, b),)
            elif direction == 'L':
                b = b-1
                self.coordinate = ((a, b), (c[1][0], b))
            else: # direction == 'R'
                b = b+1
                self.coordinate = ((a, b), (c[1][0], b))
        else: # self.state == '1x2'
            if direction == 'U':
                a = a-1
                self.coordinate = ((a, b), (a, c[1][1]))
            elif direction == 'D':
                a = a+1
                self.coordinate = ((a, b), (a, c[1][1]))
            elif direction == 'L':
                self.coordinate = ((a, min(b, c[1][1])-1),)
            else: # direction == 'R'
                self.coordinate = ((a, max(b, c[1][1])+1),)
