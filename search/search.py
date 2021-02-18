# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    """
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myStack = util.Stack()
    visitedNodes = []
    # (node, actions)
    myStack.push((startingNode, []))

    while not myStack.isEmpty():
        currentNode, actions = myStack.pop()

        if problem.isGoalState(currentNode):
            return actions

        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            for successor in problem.getSuccessors(currentNode):
                nextNode, action, cost = successor
                if nextNode not in visitedNodes:
                    newAction = actions + [action]
                    myStack.push((nextNode, newAction))
    """
    fringe = util.Stack()
    visitedNodes = [problem.getStartState()]
    path = []
    fringe.push((problem.getStartState(), 'Start', 0, path))

    while not fringe.isEmpty():
        curr, direction, depth, path = fringe.pop()

        if problem.isGoalState(curr):
            return path

        successors = problem.getSuccessors(curr)

        for node in successors:
            if node[0] not in visitedNodes:
                fringe.push((node[0], node[1], node[2], path + [node[1]]))
                print(path+[node[1]])
                visitedNodes += [curr]



    return path
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Queue()
    visitedNodes = []
    # (node, actions)
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()

        if problem.isGoalState(currentNode):
            return actions

        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            for successor in problem.getSuccessors(currentNode):
                nextNode, action, cost = successor
                if nextNode not in visitedNodes:
                    newAction = actions + [action]
                    myQueue.push((nextNode, newAction))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()

    # push the start state and list of actions to get from start state to
    # pushed state (initally empty)
    # the second argument is the cumulative cost (initially 0) as the priority
    frontier.push((problem.getStartState(), []), 0)
    expanded = []
    while not frontier.isEmpty():
        item, priority = frontier.pop()
        state, actions = item
        if problem.isGoalState(state):
            return actions

        if state not in expanded:
            expanded.append(state)
            successors = problem.getSuccessors(state)
            for succ in successors:
                nextState, action, cost = succ
                if nextState not in expanded:
                    frontier.push((nextState, actions + [action]), priority + cost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # create new PriorityQueue
    frontier = util.PriorityQueue()

    # push the start state, list of actions to get from start state to
    # pushed state (initally empty), and cumulative cost (g which initally is 0)
    # the second argument is the total cost f as the priority
    # f = g + h (cumulative cost + heuristic)
    startState = problem.getStartState()
    frontier.push((startState, [], 0), heuristic(startState, problem))
    expanded = []
    while not frontier.isEmpty():
        item, f = frontier.pop()
        state, actions, g = item
        if problem.isGoalState(state):
            return actions

        if state not in expanded:
            expanded.append(state)
            successors = problem.getSuccessors(state)
            for succ in successors:
                nextState, action, cost = succ
                next_g = g + cost
                next_h = heuristic(nextState, problem)
                next_f = next_g + next_h
                if nextState not in expanded:
                    frontier.push((nextState, actions + [action], next_g), next_f)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch