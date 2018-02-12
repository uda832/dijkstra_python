# Author: Uda Yeruultsengel
# Dijkstra Solver
# 02/11/2018

import time
import heapq
import math

class ShortestPathSolver:

    def __init__(self, start, goal, table):
        self.start = start
        self.goal = goal
        self.table = table
        self.heap = []
        self.shortestPath = []
        self.nodes = None

    def find_shortest_path(self):
        print("Starting vertex: {}".format(self.start))
        print("Ending vertex: {}".format(self.goal))

        
        ''' 
            Structure of Node: (idOfNode, costFromStart, idOfParent)
        '''

        # print("DEBUG: curNode = {} and grab_edges(curNode) = {}".format(curNode, self.grab_edges(curNode)))



        self.nodes = self.build_vertices_list()
        self.heap = []       # list of nodes (where node is a tuple in the following format: (id, idOfParent)
        distances = {x: math.inf for x in self.nodes}  # Dict of distances where the id of the node is used as key
        closedDict = {}
        goalNode = None

        # Insert start nodes into the heap
        self.heap.append((self.start, -999))       # Note: init the root node's parent to -999 to indicate null
        distances[self.start] = 0

        # Continue until the heap is empty
        while self.heap:
            self.heap.sort(reverse=True, key=lambda x: distances[x[0]]) # sort the list to emulate a min-heap
            curNode = self.heap.pop()
            closedDict[curNode[0]] = curNode    # Insert current node to the closedDict

            print("\tDEBUG: curNode = {}".format(curNode))

            if self.goal == curNode[0]:
                goalNode = curNode

            for edge in self.grab_edges(curNode):
                adjNodeId = edge[1]
                newCost = distances[curNode[0]] + edge[2]

                print("\t\tDEBUG: curNode's children = {}".format(adjNodeId))

                if (adjNodeId not in closedDict) or (newCost < distances[adjNodeId]):
                    distances[adjNodeId] = newCost

                    # Insert into self.heap if it doesn't exist
                    # Update value if it already does
                    adjNode = (adjNodeId, curNode[0])
                    self.decrease_priority(adjNode)
                        

            print("\t\tDEBUG: curNode = {} and self.heap contents = {}".format(curNode, [ (x, distances[x[0]]) for x in self.heap ]))
            print("\t\t\tDEBUG: closedDict = {}".format(closedDict))
        ###end-while

            
        self.build_shortest_path(goalNode, closedDict)
        
    ###end-find_shortest_path



    def decrease_priority(self, node):
        '''
        This function checks if the current adjacent node exists in the heap.
            - If it already exists, it updates the entry (so that the parent id is correct)
            - Else, it adds it to the heap
        '''

        updated = False
        for i,n in enumerate(self.heap):
            if n[0] == node[0]:
                self.heap[i] = node
                updated = True
                break

        if updated == False:
            self.heap.append(node)
    ###end-decrease_priority


    def build_shortest_path(self, goalNode, closedDict):
        '''
            This method backtracks from the goal node to the root node by
            iterating over the closed list and builds the shortest path and
            populates the data member self.shortestPath
        '''
        solution = []
    
        curNode = goalNode


        print("\n\nStarting build_shortest_path")


        # Iterate over closedDict following each node's parent and populate the solution list until the root is reached
        while True:


            print("\t\tDEBUG: curNode = {} and solution = {}".format(curNode, solution))


            parentId = curNode[1]

            # Root reached
            if parentId == -999:
                print("Breaking inside parent checker")
                break

            for edge in self.table:
                if edge[0] == parentId and edge[1] == curNode[0]:
                    solution.append(edge)
                    break

            try:
                curNode = [closedDict[x] for x in closedDict if closedDict[x][0] == parentId][0]
            except:
                print("ERROR(1): curNode not found in closedDict ")
                print(solution)
                solution = None
                break
        ###end-while
            
        if solution:
            self.shortestPath = solution
        else:
            self.shortestPath = []
            print("ERROR(2): function build_shortest_path failed")

    ###end-build_shortest_path

    def build_vertices_list(self):
        nodes = []
        for edge in self.table:
            if edge[0] not in nodes:
                nodes.append(edge[0])
            if edge[1] not in nodes:
                nodes.append(edge[1])
        return nodes
    ###end-function

    def grab_edges(self, node):
        # Note: 
            # edge[0] is the id of the source node
            # node[1] is the id of the current node
        # Return all edges that go out from the current node
        return [edge for edge in self.table if edge[0] == node[0]]
    ###end-grab_edges


            

    def print_shortest_path(self):
        for edge in reversed(self.shortestPath):
            print("Vertex {} to vertex {} (edge weight of {})".format(edge[0], edge[1], edge[2]))
    ###end-print-path
###end-class


def main():
    # Read from file and build transition table
    '''
        Input file format:
            Each line represents an edge with the associated cost
            Last line of the file represents the start state and the goal state
    '''

    # Read from the file and build the transition table
    f = open("input.txt", "r") 
    transitionTable = []
    for line in f:
        edge = [int(x.strip()) for x in line.split(" ") if x not in ["", "\n"]]
        transitionTable.append(tuple(edge))

    # Grab the start and goal state
    initial, final = transitionTable.pop()

    # Initialize the solver object
    pathSolver = ShortestPathSolver(initial, final, transitionTable)

    # Invoke the function to find the shortest path
    pathSolver.find_shortest_path()

    # Print the output
    pathSolver.print_shortest_path()
# end-main


main()
