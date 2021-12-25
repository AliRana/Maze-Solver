class Node():

    """A node class for A* Pathfinding"""



    def __init__(self, parent=None, position=None):

        self.Parent = parent

        self.Position = position



        self.Distance = 0

        self.Heuristic = 0

        self.TotalCost = 0



    def __eq__(self, other):

        return self.Position == other.Position





def AStar(Maze, StartPosition, EndPosition):

    """Returns a list of tuples as a path from the given start to the given end in the given maze"""



    # Create start and end node

    StartNode = Node(None, StartPosition)

    StartNode.Distance = StartNode.Heuristic = StartNode.TotalCost = 0

    EndNode = Node(None, EndPosition)

    EndNode.Distance = EndNode.Heuristic = EndNode.TotalCost = 0



    # Initialize both open and closed list

    ListOpen = []

    ListClosed = []



    # Add the start node

    ListOpen.append(StartNode)



    # Loop until you find the end

    while len(ListOpen) > 0:



        # Get the current node

        CurrentNode = ListOpen[0]

        CurrentIndex = 0

        for index, item in enumerate(ListOpen):

            if item.TotalCost < CurrentNode.TotalCost:

                CurrentNode = item

                CurrentIndex = index



        # Pop current off open list, add to closed list

        ListOpen.pop(CurrentIndex)

        ListClosed.append(CurrentNode)



        # Found the goal

        if CurrentNode == EndNode:

            Path = []

            Current = CurrentNode

            while Current is not None:

                Path.append(Current.Position)

                Current = Current.Parent

            return Path[::-1] # Return reversed path



        # Generate children

        Children = []

        for NewPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares



            # Get node position

            NodePosition = (CurrentNode.Position[0] + NewPosition[0], CurrentNode.Position[1] + NewPosition[1])



            # Make sure within range

            if NodePosition[0] > (len(Maze) - 1) or NodePosition[0] < 0 or NodePosition[1] > (len(Maze[len(Maze)-1]) -1) or NodePosition[1] < 0:

                continue



            # Make sure walkable terrain

            if Maze[NodePosition[0]][NodePosition[1]] != 0:

                continue



            # Create new node

            NewNode = Node(CurrentNode, NodePosition)



            # Append

            Children.append(NewNode)



        # Loop through children

        for ChildNode in Children:



            # Child is on the closed list

            for ChildNode_Closed in ListClosed:

                if ChildNode == ChildNode_Closed:

                    continue



            # Create the Distance, Heuristic and TotalCost values

            ChildNode.Distance = CurrentNode.Distance + 1

            ChildNode.Heuristic = ((ChildNode.Position[0] - EndNode.Position[0]) ** 2) + ((ChildNode.Position[1] - EndNode.Position[1]) ** 2)

            ChildNode.TotalCost = ChildNode.Distance + ChildNode.Heuristic



            # Child is already in the open list

            for NodeOpen in ListOpen :

                if ChildNode == NodeOpen and ChildNode.Distance > NodeOpen.Distance:

                    continue



            # Add the child to the open list

            ListOpen.append(ChildNode)





def main():



    Maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



    StartPosition = (0, 0)

    EndPosition = (9, 9)



    Path = AStar(Maze, StartPosition, EndPosition)
    print(Path)





if __name__ == '__main__':

    main()
