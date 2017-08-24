def flatten(nested_list):
    for value in nested_list:
        if isinstance(value, list):
            for nested_value in flatten(value):
                yield nested_value
            else:
                yield value

def some(nested_list, fn):
    for value in flatten(nested_list):
        if fn(value):
            return value
    return None

class Cell(set):
    def __init__(self, y, x):
        self.marked = False
        self.y = y
        self.x = x
        self.update(range(1, 10))

    def is_explicit(self):
        return len(self) == 1

    def mark(self, value):
        self.marked = True
        self.clear()
        self.add(value)

    def set(self, values):
        self.marked = False
        self.clear()
        self.update(values)

    def value(self):
        return next(iter(self))

    def __str__(self):
        size = len(self)
        if size == 0:
            return 'X'
        elif size == 1:
            return str(self.value())
        else:
            return '?'

class Table:
    def __init__(self):
        self.values = [[Cell(y, x) for x in xrange(9)] for y in xrange(9)]

    def is_valid(self):
        return all(flatten(self.values))

    def is_finished(self):
        return all([e.is_explicit() for e in flatten(self.values)])

    def first_implicit(self):
        return some(self.values, lambda e: not e.is_explicit())

    def first_explicit(self):
        return some(self.values, lambda e: not e.marked and e.is_explicit())

    def get_neighbors(self, y, x):
        neighbors = []
        # horizontal
        neighbors.extend([self.values[y][c] for c in xrange(9) if c != x and not self.values[y][c].marked])
        # vertical
        neighbors.extend([self.values[r][x] for r in xrange(9) if r != y and not self.values[r][x].marked])
        # box
        start_x = x / 3 * 3
        start_y = y / 3 * 3
        for r in range(start_y, start_y + 3):
            for c in range(start_x, start_x + 3):
                if r != y and c != x and not self.values[r][c].marked:
                    neighbors.append(self.values[r][c])
        return neighbors

    def __str__(self):
        return '\n'.join([' '.join(str(c) for c in r) for r in self.values])

class Command:
    def __init__(self, table, y, x, value):
        self.table = table
        self.y = y
        self.x = x
        self.value = value
        self.cell = table.values[y][x].copy()
        self.queue = []
        self.executed = False

    def redo(self):
        if self.executed:
            return
        else:
            self.executed = True
        self.queue = []
        for cell in self.table.get_neighbors(self.y, self.x):
            if self.value in cell:
                cell.remove(self.value)
                self.queue.append(cell)
        self.table.values[self.y][self.x].mark(self.value)

    def undo(self):
        if self.executed:
            self.executed = False
        else:
            return
        for cell in self.queue:
            cell.add(self.value)
        self.table.values[self.y][self.x].set(self.cell)

class Sudoku:
    def __init__(self):
        self.table = Table()
        self.queue = []

    def push(self, y, x, value):
        cmd = Command(self.table, y, x, value)
        cmd.redo()
        self.queue.append(cmd)

    def pop(self):
        cmd = self.queue.pop()
        cmd.undo()

    def load(self, matrix):
        for y, line in zip(range(9), matrix.strip().split('\n')):
            for
2000
x, value in zip(range(9), line.strip().split(' ')):
            if value != '?':
                    self.push(y, x, int(value))
        self.derive()
 
    def derive(self):
        count = 0
        while True:
            cell = self.table.first_explicit()
            if cell:
                self.push(cell.y, cell.x, cell.value())
                count += 1
            else:
                return count
 
    def revert(self, deep):
        for i in xrange(-1, deep):
            self.pop()
 
    def bfs(self):
        cell = self.table.first_implicit()
        for value in cell.copy():
            self.push(cell.y, cell.x, value)
            deep = self.derive()
            if self.table.is_finished():
                return True
            elif not self.table.is_valid():
                self.revert(deep)
            else:
                result = self.bfs()
                if result:
                    return True
                else:
                    self.revert(deep)
        return False
 
    def __str__(self):
        return str(self.table)
 
puzzle = '''
? ? ? ? ? 7 ? 8 2
5 ? 7 ? ? ? 4 ? ?
? ? ? 2 5 ? ? ? ?
8 ? 9 1 7 ? ? ? ?
? 7 ? 5 ? 3 6 ? 8
? 5 3 ? ? ? ? 9 1
2 ? ? ? ? ? 3 ? 6
? ? ? 3 ? 2 ? ? ?
? 8 5 ? 6 ? ? ? ?
'''
sudoku = Sudoku()
sudoku.load(puzzle)
sudoku.bfs()
print sudoku