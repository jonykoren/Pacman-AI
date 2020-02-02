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

# Getting the current state, parent and action

class Node:
    
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action



def path_helper(node):
    """
    insert the parent of the node to the beginning of the specified fringe 
    and update path --> for accumulated cost
    """
    path = []
    while node.parent is not None:
        path.insert(0, node.action)
        node = node.parent
    return path





def graphSearch(problem, visited, fringe):
    """
    graph search:
    A routine process for the methods: DFS , BFS , Uniform-Cost-Search, A*
    return a successful path if exists
    """
    # Defining a start values for state, parent and action
    start = Node(problem.getStartState(), None, None)
    # Push the first 1 from the specified fringe
    fringe.push(start)
    # if the specified fringe is not empty
    while not fringe.isEmpty():
        # Remove the 1st path from the specified fringe
        node = fringe.pop()
        # and while the goal!=True
        if problem.isGoalState(node.state):
            # Create new paths to all children
            return path_helper(node)
        # add expanding node into the visited if not happen yet
        if node.state not in visited:
            visited.add(node.state)
            # For path in paths
            for child_node in problem.getSuccessors(node.state):
                # add the new nodes to the specified fringe
                state, action, cost = child_node
                # push the next path from the specified fringe
                fringe.push(Node(state, node, action))



"******************"


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
    a list of actions that reaches the goal by DFS
    """
    # Stack Settings
    return graphSearch(problem, visited=set(), fringe=util.Stack())


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Queue Settings
    return graphSearch(problem, visited=set(), fringe=util.Queue())


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Priority Queue Settings with accumulated cost function
    fn = lambda node: problem.getCostOfActions(path_helper(node))
    return graphSearch(problem, visited=set(), fringe=util.PriorityQueueWithFunction(fn))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Priority Queue Settings with accumulated cost function + Heuristic "accumulated cost" function
    fn = lambda node: problem.getCostOfActions(path_helper(node)) + heuristic(node.state, problem)
    return graphSearch(problem, visited=set(), fringe=util.PriorityQueueWithFunction(fn))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
