# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    from util import Stack
    start_state = problem.getStartState()
    curr_state = problem.getStartState()
    s = util.Stack()
    greyset = set()
    parentpointers = {}
    parentpointers[curr_state] = start_state


    while not problem.isGoalState(curr_state):
        for x in problem.getSuccessors(curr_state):

            if (x[0] in greyset)== False:
                s.push(x[0])
                parentpointers[x[0]] = [curr_state,x[1],x[2]]

        greyset.add(curr_state)
        curr_state = s.pop()



    result = []

    if(problem.isGoalState(curr_state)):
        while (parentpointers[curr_state]!= start_state):

            result.append(parentpointers[curr_state][1])
            curr_state=parentpointers[curr_state][0]
    result.reverse()


    return result







    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    from util import Queue
    start_state = problem.getStartState()
    curr_state = problem.getStartState()
    s = util.Queue()
    greyset = set()
    parentpointers = {}
    parentpointers[curr_state] = start_state

    while not problem.isGoalState(curr_state):

        for x in problem.getSuccessors(curr_state):

            if (x[0] in greyset) == False:
                s.push(x[0])
                parentpointers[x[0]] = [curr_state, x[1], x[2]]
                greyset.add(x[0])

        greyset.add(curr_state)
        curr_state = s.pop()








    result = []

    if (problem.isGoalState(curr_state)):
        while (parentpointers[curr_state] != start_state):
            result.append(parentpointers[curr_state][1])
            curr_state = parentpointers[curr_state][0]
    result.reverse()

    return result
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    start_state = problem.getStartState()
    curr_state = problem.getStartState()
    s = util.PriorityQueue()
    cost = {}
    cost[curr_state]= 0
    frontier =set()
    frontier.add(curr_state)


    greyset = set()
    parentpointers = {}
    parentpointers[curr_state] = start_state


    while not problem.isGoalState(curr_state):
        greyset.add(curr_state)
        for x in problem.getSuccessors(curr_state):


            if (x[0] in greyset)== False:
                if(not x[0] in frontier):

                    cost[x[0]] = cost[curr_state]+x[2]
                    s.push(x[0],cost[x[0]])
                    frontier.add(x[0])
                    parentpointers[x[0]] = [curr_state,x[1],x[2]]


                else:
                    if cost[x[0]]>cost[curr_state]+x[2]:

                        cost[x[0]] = cost[curr_state]+x[2]



                        s.push(x[0],cost[x[0]])
                        parentpointers[x[0]] = [curr_state, x[1], x[2]]


        frontier.remove(curr_state)
        curr_state = s.pop()
        while not curr_state in frontier:

            curr_state = s.pop()





    result = []

    if(problem.isGoalState(curr_state)):
        while (parentpointers[curr_state]!= start_state):

            result.append(parentpointers[curr_state][1])
            curr_state=parentpointers[curr_state][0]
    result.reverse()


    return result

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    curr_state = problem.getStartState()
    s = util.PriorityQueue()
    cost = {}
    cost[curr_state] = 0

    pathcost = {}
    pathcost[curr_state]=0

    frontier = set()
    frontier.add(curr_state)

    greyset = set()
    parentpointers = {}
    parentpointers[curr_state] = start_state

    while not problem.isGoalState(curr_state):
        greyset.add(curr_state)
        for x in problem.getSuccessors(curr_state):

            if (x[0] in greyset) == False:
                if (not x[0] in frontier):

                    cost[x[0]] = pathcost[curr_state] + x[2]+heuristic(x[0],problem)
                    pathcost[x[0]] = pathcost[curr_state]+x[2]
                    s.push(x[0], cost[x[0]])
                    frontier.add(x[0])
                    parentpointers[x[0]] = [curr_state, x[1], x[2]]


                else:
                    if cost[x[0]] > pathcost[curr_state] + x[2]+heuristic(x[0],problem):
                        cost[x[0]] = pathcost[curr_state] + x[2] + heuristic(x[0], problem)
                        pathcost[x[0]] = pathcost[curr_state] + x[2]



                        s.push(x[0], cost[x[0]])
                        parentpointers[x[0]] = [curr_state, x[1], x[2]]


        frontier.remove(curr_state)
        curr_state = s.pop()
        while not curr_state in frontier:

            curr_state = s.pop()


    result = []

    if (problem.isGoalState(curr_state)):
        while (parentpointers[curr_state] != start_state):
            result.append(parentpointers[curr_state][1])
            curr_state = parentpointers[curr_state][0]
    result.reverse()

    return result


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
