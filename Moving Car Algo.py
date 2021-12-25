import time

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

 
        #Pop current off open list, add to closed list 
        ListOpen.pop(CurrentIndex) 
        ListClosed.apend(CurrentNode) 

 

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
            NodePosition = (NewPosition[0],NewPosition[1]) 

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
            
def MovingCar(path,StartPosition,EndPosition): 
    try: 
        print(path) 
        print(path[5][0]) 
        CurrentVector = StartPosition 
        PreVector = [StartPosition] 
        NextVector = [] 
        count = 0 
        print("Number of Turns needed to get to exit location", len(path)-1) 
        for i in path: 
            if count < len(path): 
                print() 
                NextVector = path[count + 1] 
                X_coordinate = NextVector[0] 
                Y_coordinate = NextVector[1] 
                NewNextVector = path[count+2] 
                NewX_coordinate = NewNextVector[0] 
                NewY_coordinate = NewNextVector[1] 
                X_Direction = NewX_coordinate - X_coordinate 
                Y_Direction = NewY_coordinate - Y_coordinate 
                print("NextVector is", NextVector) 
                print("X Co-ordinate of Next Vector is", X_coordinate) 
                print("Y Co-ordinate of Next Vector is", Y_coordinate) 
                print("NewNextVector is", NewNextVector) 
                print("NewX Co-ordinate of New Next Vector is", NewX_coordinate) 
                print("NewY Co-ordinate of New Next Vector is", NewY_coordinate) 
                print("New X Direction", X_Direction) 
                print("New Y Direction", Y_Direction) 
                if X_Direction == 1 and Y_Direction == 0: 
                    print("Moving North") 
                    #North() 
                elif X_Direction == 1 and Y_Direction == 1: 
                    print("Moving NorthWest") 
                    #NorthWest() 
                elif X_Direction == 0 and Y_Direction == 1: 
                    print("Moving West") 
                    #West() 
                elif X_Direction ==-1 and Y_Direction == 1: 
                    print("Moving SouthWest") 
                    #SouthWest() 
                elif X_Direction == -1 and Y_Direction == 0: 
                    print("Moving South") 
                    #South() 
                elif X_Direction == -1 and Y_Direction == -1: 
                    print("Moving SouthEast") 
                    #SouthEast() 
                elif X_Direction == 0 and Y_Direction == -1: 
                    print("Moving East") 
                    #East() 
                elif X_Direction == 1 and Y_Direction == -1: 
                    print("Moving NorthEast") 
                    #NorthEast() 
            count +=  1 
    except:
        print("Too Big")

def main():
    
    Maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    StartPosition = (0, 0) 
    EndPosition = (9, 9) 
    Path = AStar(Maze, StartPosition, EndPosition) 
    #print(Path) 
    MovingCar(Path,StartPosition,EndPosition) 

if __name__ == '__main__': 

    main() 

    

    
