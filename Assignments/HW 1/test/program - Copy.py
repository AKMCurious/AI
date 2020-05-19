# Author - Amith Kumar Matapady
# Course - CS 6364.001 Artificial Intelligence

# ------------------------------------------------------------------------
# imports

import os
import io
import sys

# -------------------------------------------------------------------------
# general methods and/or classes for all search methods


class Node:
    def __init__( self, data, level, f, parent):
        self.data = data
        self.parent = parent
        self.level = level
        self.f = f


def getBlankPosition(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '*':
                return i,j
    return -1,-1


def getPosition(grid, value):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == value:
                return i,j
    return -1,-1


def checkState(inputArr):
    global goal_grid
    for i in range(3):
        for j in range(3):
            if goal_grid[i][j] != inputArr[i][j]:
                return False
    return True


def printState(inputArr):
    for i in range(3):
        #for j in range(3):
        print(inputArr[i][0] + " " + inputArr[i][1] + " " + inputArr[i][2])
        #print("\n")
    print("\n")


def printAllStates(inputArr):
    # find the value for the array in the map and add it to the stack
    # after that pop from stack and print the array one after another
    stack = []
    curr_arr = inputArr
    stack.append(curr_arr)
    while curr_arr.parent is not None:
        curr_arr = curr_arr.parent
        stack.append(curr_arr)

    while len(stack) > 0:
        curr_arr = stack.pop()
        printState(curr_arr.data)


def getData(curr_node):
    new_data = []
    for i in range(3):
        temp = []
        for j in range(3):
           temp.append(curr_node.data[i][j])
        new_data.append(temp)
    return new_data


# ----------------------------------------------------------------------------------------------
# Breadth first search method


def bfs():
    #print("bfs algo starts\n")
    global input_node, max_depth
    queue = []
    count_enqued = 0

    if checkState(input_node.data):
        print("the input state is the goal state\n")
        print("No of moves = 0")
        print("No of states enqueued = " + str(count_enqued))
        print("No of current states to process = " + str(len(queue)))
        printState(input_node.data)
        return
    #prev_map = {}
    #prev_map[tuple(input_grid)] = input_grid;
    queue.append(input_node)
    count_enqued+=1
    #queue.append(None)
    level = 0
    #states.append(input_grid)
    while len(queue) > 0 :
        curr_node = queue.pop(0)
        level = curr_node.level
        if level > max_depth:
            print("Goal state not reached by depth 10. Failure.\n")
            break;

        curr_states = []
        #level = curr_node.level
        a, b = getBlankPosition(curr_node.data)
        if a>0: #up
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a-1][b]
            new_grid[a-1][b] = '*'
            #prev_map[new_grid] = curr_grid;
            new_node_u = Node(new_grid, level+1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_u)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(queue)))
                return
            queue.append(new_node_u)
            count_enqued += 1
        if a < 2:   #down
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a + 1][b]
            new_grid[a + 1][b] = '*'
            #prev_map[new_grid] = curr_grid;
            new_node_d = Node(new_grid, level + 1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_d)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(queue)))
                return
            queue.append(new_node_d)
            count_enqued += 1
        if b > 0:   #left
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a][b-1]
            new_grid[a][b-1] = '*'
            #prev_map[new_grid] = curr_grid;
            new_node_l = Node(new_grid, level + 1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_l)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(queue)))
                return
            queue.append(new_node_l)
            count_enqued += 1
        if b < 2:   #right
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a][b+1]
            new_grid[a][b+1] = '*'
            #prev_map[new_grid] = curr_grid;
            new_node_r = Node(new_grid, level + 1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_r)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(queue)))
                return
            queue.append(new_node_r)
            count_enqued += 1

    print("Goal state not reached by depth 10. Failure.\n")
    return


# ----------------------------------------------------------------------------------------------
# Iterative Deepening Search method


def dls(max_d):
    global input_node
    if checkState(input_node.data):
        print("the input state is the goal state\n")
        print("No of moves = 0")
        print("No of states enqueued = 0" )
        print("No of current states to process = 0")
        printState(input_node.data)
        return input_node
    level = input_node.level
    if level >= max_d:
        return None
    states =[]
    count_enqued = 1
    states.append(input_node)
    while len(states) > 0:
        curr_node = states.pop()
        level = curr_node.level
        #count_enqued += 1
        if level >= max_d:
            continue
        a, b = getBlankPosition(curr_node.data)
        if a > 0:  # up
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a - 1][b]
            new_grid[a - 1][b] = '*'
            # prev_map[new_grid] = curr_grid;
            new_node_u = Node(new_grid, level + 1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_u)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(states)))
                return new_node_u
            if (level + 1) < max_d:
                states.append(new_node_u)
                count_enqued += 1
        if a < 2:  # down
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a + 1][b]
            new_grid[a + 1][b] = '*'
            # prev_map[new_grid] = curr_grid;
            new_node_d = Node(new_grid, level + 1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_d)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(states)))
                return new_node_d
            if (level + 1) < max_d:
                states.append(new_node_d)
                count_enqued += 1

        if b > 0:  # left
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a][b - 1]
            new_grid[a][b - 1] = '*'
            # prev_map[new_grid] = curr_grid;
            new_node_l = Node(new_grid, level + 1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_l)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(states)))
                return new_node_l
            if (level + 1) < max_d:
                states.append(new_node_l)
                count_enqued += 1
        if b < 2:  # right
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a][b + 1]
            new_grid[a][b + 1] = '*'
            # prev_map[new_grid] = curr_grid;
            new_node_r = Node(new_grid, level + 1, 0, curr_node)
            if checkState(new_grid):
                printAllStates(new_node_r)
                print("No of moves = " + str(level + 1))
                print("No of states enqueued = " + str(count_enqued))
                print("No of current states to process = " + str(len(states)))
                return new_node_r
            if (level + 1) < max_d:
                states.append(new_node_r)
                count_enqued += 1
    return None


def ids():
    global max_depth
    d = 0
    res = None
    while d <= max_depth:
        res = dls(d)
        if res is not None:
            return
        d += 1
    print("Goal state not reached by depth 10. Failure.\n")
    return


# ------------------------------------------------------------------------------------------------
# A* algorithm with two heuristics - h1 (No of mismatched tiles), h2 (Manhattan distance)


# Tiles not in correct place
def h1(curr_node):
    global goal_grid
    res = 0
    for i in range(3):
        for j in range(3):
            if goal_grid[i][j] != curr_node.data[i][j]:
                res+=1
    return res


# Sum of moves required to move each tile to correct place (manhattan distance)
def h2(curr_node):
    global goal_grid
    res = 0
    for i in range(3):
        for j in range(3):
            a,b = getPosition(curr_node.data, goal_grid[i][j])
            res += abs(i-a) + abs(j-b)
    return res


def astar(heuristic):
    global input_node, goal_grid, max_depth
    if checkState(input_node.data):
        print("the input state is the goal state\n")
        print("No of moves = 0")
        print("No of states enqueued = 0")
        printState(input_node.data)
        return
    enqueued = 0
    pqueue = []
    if heuristic == 0:
        input_node.f = h1(input_node)
    else:
        input_node.f = h2(input_node)
    pqueue.append(input_node)
    enqueued += 1
    final_node = Node(input_grid, 0, float("inf"), None)
    while len(pqueue) > 0:
        pqueue.sort(key=lambda z: z.f, reverse=False)
        curr_node = pqueue.pop(0)
        if final_node.f <= curr_node.f:
            break
        level = curr_node.level
        a, b = getBlankPosition(curr_node.data)
        if a > 0:  # up
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a - 1][b]
            new_grid[a - 1][b] = '*'
            new_node_u = Node(new_grid, level + 1, 0, curr_node)
            if heuristic == 0:
                new_node_u.f = h1(new_node_u)
            else:
                new_node_u.f = h2(new_node_u)
            if checkState(new_grid):
                if final_node.f > new_node_u.f:
                    final_node.data = getData(new_node_u)
                    final_node.f = new_node_u.f
                    final_node.level = new_node_u.level
                    final_node.parent = new_node_u.parent
            elif (level + 1) < max_depth:
                pqueue.append(new_node_u)
                enqueued += 1
        if a < 2:  # down
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a + 1][b]
            new_grid[a + 1][b] = '*'
            new_node_d = Node(new_grid, level + 1, 0, curr_node)
            if heuristic == 0:
                new_node_d.f = h1(new_node_d)
            else:
                new_node_d.f = h2(new_node_d)
            if checkState(new_grid):
                if final_node.f > new_node_d.f:
                    final_node.data = getData(new_node_d)
                    final_node.f = new_node_d.f
                    final_node.level = new_node_d.level
                    final_node.parent = new_node_d.parent
            elif (level + 1) < max_depth:
                pqueue.append(new_node_d)
                enqueued += 1
        if b > 0:  # left
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a][b - 1]
            new_grid[a][b - 1] = '*'
            new_node_l = Node(new_grid, level + 1, 0, curr_node)
            if heuristic == 0:
                new_node_l.f = h1(new_node_l)
            else:
                new_node_l.f = h2(new_node_l)
            if checkState(new_grid):
                if final_node.f > new_node_l.f:
                    final_node.data = getData(new_node_l)
                    final_node.f = new_node_l.f
                    final_node.level = new_node_l.level
                    final_node.parent = new_node_l.parent
            elif (level + 1) < max_depth:
                pqueue.append(new_node_l)
                enqueued += 1
        if b < 2:  # right
            new_grid = getData(curr_node)
            new_grid[a][b] = new_grid[a][b + 1]
            new_grid[a][b + 1] = '*'
            new_node_r = Node(new_grid, level + 1, 0, curr_node)
            if heuristic == 0:
                new_node_r.f = h1(new_node_r)
            else:
                new_node_r.f = h2(new_node_r)
            if checkState(new_grid):
                if final_node.f > new_node_r.f:
                    final_node.data = getData(new_node_r)
                    final_node.f = new_node_r.f
                    final_node.level = new_node_r.level
                    final_node.parent = new_node_r.parent
            elif (level + 1) < max_depth:
                pqueue.append(new_node_r)
                enqueued += 1

    if final_node.f < float("inf"):
        printAllStates(final_node)
        print("No of moves = " + str(final_node.level))
        print("No of states enqueued = " + str(enqueued))
    else:
        print("Goal state not reached by depth 10. Failure.\n")
    return


# ------------------------------------------------------------------------------------------------
# Program flow/execution starts below


algo = ""
if (len(sys.argv) > 1):
    algo = sys.argv[1]

if(len(algo) < 1):
    print("No algorithm selected")
    exit(0)
max_depth = 10
input_grid = []
goal_grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '*']]
input_node = Node(input_grid, 0, 0, None)
print("\nEnter the 3x3 grid of tiles (Enter * for blank tile. Use 1-8 for the rest)")
while True:
    for i in range(3):
        sub = []
        sub = input().split()
        while len(sub) != 3:
            sub = input().split()
        input_grid.append(sub)
    print("\n")
    input_node = Node(input_grid, 0, 0, None)
    a, b = getBlankPosition(input_grid)
    if (a < 0 or b < 0):
        print("No blank tile in input")
    else:
        break

if algo == "bfs":
    bfs()
elif algo == "ids":
    ids()
elif algo == "astar1":
    astar(0)
elif algo == "astar2":
    astar(1)
else:
    print("Incorrect algorithm name entered\n")


