import copy
class cuboid1x1x2():
    def __init__(self, coordinate, grid):
        self.coordinate = coordinate # tuple of tuples
        self.path = '' # string of direction
        self.recall = '' # string of reverse direction
        self.grid = grid # set of tuples
    @property
    def state(self):
        c = self.coordinate
        if len(c) == 1:
            return '1x1'
        elif c[0][1] == c[1][1]:
            return '2x1'
        else: # c[0][0] == c[1][0]
            return '1x2'
    @property
    def is_in_bound(self): # grid is a set of tuples
        return (set(self.coordinate).issubset(self.grid))
    
    @staticmethod
    def opposite(direction):
        if (direction == 'U'):
            return 'D'
        elif (direction == 'D'):
            return 'U'
        elif (direction == 'L'):
            return 'R'
        else:# (direction == 'R'):
            return 'L'
    
    def roll(self, direction): # direction is a string from U, D, L, R
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
