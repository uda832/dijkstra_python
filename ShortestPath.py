import heapq
import math

class ShortestPathSolver:

    def __init__(self, start, goal, table):
        self.start = start
        self.goal = goal
        self.table = table

    def find_shortest_path(self):
        print("Starting vertex: {}".format(self.start))
        print("Ending vertex: {}".format(self.goal))

        
        ''' 
            Structure of Node: (idOfNode, costFromStart, idOfParent)
        '''

        self.shortestPath = []
        heap = []               # Initialize priority queue (i.e. min-heap)
        closedDict = {}         # Initilize the closed dict (i.e. discovered nodes)
        distances = {}

        # Insert the start node
        startNode = (self.start, 0, -99)                  # Note structure of node ( nodeId,costFromStart, parentId)
        # heapq.heappush(heap, startNode)
        heap.append(startNode)
        heap.sort(reverse=True, key=lambda x: x[1])
        

        # While the heap is not empty
        while heap:
            heap.sort(reverse=True, key=lambda x: x[1])
            # curNode = heapq.heappop(heap)
            curNode = heap.pop()

            print("DEBUG: current minimum node -- {}".format(curNode))
            print("\t\tDEBUG: current contents of heap -- {}".format(heap))
            print("\t\tDEBUG: current contents of closedDict -- {}".format(closedDict))

            pathCost = curNode[1]                   # Distance to current node from the start node
            closedDict[curNode[0]] = curNode        # Insert into closedDict using the id as key

            # Check if goal is reached
            if self.goal == curNode[0]:
                self.build_shortest_path(curNode, closedDict)
                break
            
            for edge in self.grab_edges(curNode):
                adjNodeId = edge[1]                   # Grab id of the destination/adj node
                edgeCost = edge[2]
                newCost = edgeCost + pathCost

                print("\tDEBUG: {}'s child node -- {}".format(curNode, adjNodeId))

                adjNodeContainer = [x for x in heap if x[0] == adjNodeId]

                print("\tDEBUG: adjNodeContainer = {}".format(adjNodeContainer))

                adjNodePathCost = adjNodeContainer[0][1] if (len(adjNodeContainer) > 0) else math.inf



                print("\tDEBUG: adjNodePathCost = {}".format(adjNodePathCost))


                
                boolB = newCost < adjNodePathCost

                if adjNodeId not in closedDict:
                    print("\t\t\tDEBUG: boolA = {} and boolB = {}".format(boolA, boolB))

                    # If the currenct adjNode does not exist in the heap (i.e. fringe), add it 
                    # Else, update the pathCost
                    if len(adjNodeContainer) == 0:
                        node = (newCost, adjNodeId, curNode[1]) # (pathCost, nodeId, parentId)
                        # heapq.heappush(heap, node)
                        heap.append(node)
                    else:
                        for i, node in enumerate(heap):
                            if node[1] == adjNodeId:
                                heap[i] = (newCost, node[1], node[2])   # replace the tuple
                                # heapq.heapify(heap)                           # update the heap
                                heap.sort(reverse=True, key=lambda x: x[1])

            print("\t\tDEBUG: current contents of heap -- {}".format(heap))

        # Return solution
        self.shortestPath 

    ###end-shortest_path

    def build_shortest_path(self, goalNode, closedDict):
        '''
            This method backtracks from the goal node to the root node by
            iterating over the closed list and builds the shortest path and
            populates the data member shortestPath
        '''
        solution = []
    
        curNode = goalNode
        # Iterate over closedDict following each node's parent and populate the solution list until the root is reached
        while True:
            parentId = curNode[2]
            childId = curNode[1]

            # Root reached
            if parentId == -99:
                break

            for edge in self.table:
                if edge[0] == parentId and edge[1] == childId:
                    solution.append(edge)
                    break
            try:
                curNode = [x for x in closedDict if x[1] == parentId][0]
            except:
                print("ERROR(1): curNode not found in closedDict ")
                print(solution)
                solution = None
                break
            
        if solution:
            self.shortestPath = solution
        else:
            self.shortestPath = None
            print("ERROR(2): function failed")
    ###end-build_shortest_path



    def grab_edges(self, node):
        # Note: 
            # edge[0] is the id of the source node
            # node[1] is the id of the current node
        # Return all edges that go out from the current node
        return [edge for edge in self.table if edge[0] == node[1]]
    ###end-grab_edges


            

    def print_shortest_path(self):
        for edge in self.shortestPath:
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
