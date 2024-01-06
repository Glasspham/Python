import copy
from queue import PriorityQueue
import time
import random

class State:
    def __init__(self, data=None, par=None, g=0, h=0, op=None):
        self.data = data
        self.par = par
        self.g = g
        self.h = h
        self.op = op

    def clone(self):
        sn = copy.deepcopy(self)
        return sn

    def Print(self):
        sz = 3
        for i in range(sz):
            for j in range(sz):
                print(self.data[i * sz + j], end=' ')
            print()
        print()

    def Key(self):
        if self.data is None:
            return None
        res = ' '
        for x in self.data:
            res += str(x)
        return res

    def __lt__(self, other):
        if other is None:
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if other is None:
            return False
        return self.Key() == other.Key()

class Operator:
    def __init__(self, i):
        self.i = i

    def checkStateNull(self, s):
        return s.data is None

    def findPos(self, s):
        sz = 3
        for i in range(sz):
            for j in range(sz):
                if s.data[i * sz + j] == 0:
                    return i, j
        return None

    def swap(self, s, x, y, i):
        sz = 3
        sn = s.clone()
        x_new = x
        y_new = y

        if i == 0:
            x_new = x + 1
            y_new = y
        if i == 1:
            x_new = x - 1
            y_new = y
        if i == 2:
            x_new = x
            y_new = y + 1
        if i == 3:
            x_new = x
            y_new = y - 1

        sn.data[x * sz + y] = sn.data[x_new * sz + y_new]
        sn.data[x_new * sz + y_new] = 0
        return sn

    def up(self, s):
        if self.checkStateNull(s):
            return None
        pos = self.findPos(s)
        if pos is None:
            return None
        x, y = pos
        if x == 2:
            return None
        return self.swap(s, x, y, self.i)


    def down(self, s):
        if self.checkStateNull(s):
            return None
        pos = self.findPos(s)
        if pos is None:
            return None
        x, y = pos
        if x == 0:
            return None
        return self.swap(s, x, y, self.i)


    def left(self, s):
        if self.checkStateNull(s):
            return None
        pos = self.findPos(s)
        if pos is None:
            return None
        x, y = pos
        if y == 2:
            return None
        return self.swap(s, x, y, self.i)


    def right(self, s):
        if self.checkStateNull(s):
            return None
        pos = self.findPos(s)
        if pos is None:
            return None
        x, y = pos
        if y == 0:
            return None
        return self.swap(s, x, y, self.i)

    def move(self, s):
        if self.i == 0:
            return self.up(s)
        if self.i == 1:
            return self.down(s)
        if self.i == 2:
            return self.left(s)
        if self.i == 3:
            return self.right(s)
        return None

def checkInPriority(Open, tmp):
    if tmp is None:
        return False
    return tmp in Open.queue

def equal(O, G):
    if O is None:
        return False
    return O.Key() == G.Key()

def Path(O, steps=None):
    if steps is None:
        steps = []
    if O.par is not None:
        steps = Path(O.par, steps)
        steps.append(O.op.i)
    O.Print()
    return steps

def Hx(S, G):
    sz = 3
    res = 0
    for i in range(sz):
        for j in range(sz):
            val = S.data[i * sz + j]
            if val != 0:
                x_goal = (val - 1) // sz
                y_goal = (val - 1) % sz
                res += abs(i - x_goal) + abs(j - y_goal)
    return res

def RUN(S, G):
    Open = PriorityQueue()
    closed_set = set()
    S.g = 0
    S.h = Hx(S, G)
    Open.put(S)

    while not Open.empty():
        O = Open.get()
        if equal(O, G):
            print('Tim thay')
            steps = Path(O)
            print("Bước giải:", steps)
            return
        
        closed_set.add(O.Key())
        for i in range(4):
            op = Operator(i)
            child = op.move(O)
            if child is None:
                continue

            child_key = child.Key()
            if child_key not in closed_set:
                child.par = O
                child.op = op
                child.g = O.g + 1
                child.h = Hx(child, G)
                Open.put(child)
                closed_set.add(child_key)

    print('Tim kiem that bai')

def isSolvable(start, goal):
    inv_count_start = countInversions(start)
    inv_count_goal = countInversions(goal)
    return (inv_count_start % 2 == inv_count_goal % 2)

def countInversions(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] and arr[j] and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# Assuming you have an init function that initializes the starting and goal states
def init():
    start = list(range(9))
    random.shuffle(start)
    goal = sorted(start)

    if not isSolvable(start, goal):
        print("Không có lời giải cho trạng thái ban đầu và trạng thái đích này.")
        return None, None

    S = State(data=start)
    G = State(data=goal)
    return S, G

S, G = init()
if S is not None and G is not None:
    S.Print()
    G.Print()
    t1 = time.time()
    RUN(S, G)
    t2 = time.time()
    print('time: ', (t2 - t1))
