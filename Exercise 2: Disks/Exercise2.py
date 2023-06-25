class Node:
    def __init__(self,disk,width,depth,height,parent):
        self.disk      = disk
        self.width     = width
        self.depth     = depth
        self.height    = height
        self.sumHeight = height
        self.parent    = parent

def diskStacking(disks):
        #Sort the disks according to 'height' in accending order
        disks.sort(key=lambda x: x[2])
        
        #Create a node object for each disk in disks
        nodes = []
        for disk in disks:
            node = Node(disk,disk[0],disk[1],disk[2],None)
            nodes.append (node)
                
        #loop the disks to check which disk can be stacked over the other
        for i in range(1,len(nodes)):
            for j in range(i):
                if canStackUp(nodes[j], nodes[i]):
                    if (nodes[j].sumHeight + nodes[i].height > nodes[i].sumHeight):
                        nodes[i].sumHeight = nodes[j].sumHeight + nodes[i].height
                        nodes[i].parent = nodes[j]
                        
        #find the node with max height
        maxHeightNode = max(nodes, key=lambda x: x.sumHeight)
        return getFinalStack(maxHeightNode)
                
def canStackUp(above,below):
    #Placing the disk with smaller dimensions above the bigger dimension disk
    if (above.width < below.width and
        above.depth < below.depth and
        above.height < below.height ):
        return True
    else:
        return False
    
def getFinalStack(node):
    FinalStack = []
    while(node):
        FinalStack.append(node.disk)
        node = node.parent                  #backtrack with the parent node stored
    return FinalStack
        
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
print(diskStacking(disks))

#> Time complexity  : O(N^2) : 
#> N is the nummber of disks.
#> Since each N disk is compared to every other N disks for dimension comparision, we traverse two nested 'for' loops.
#> Resulting in worst case time complexity of O(N^2)

#> Space complexity : O(N^2) : 
#> N is each disk node created.
#> N spaces are allocated for N disk nodes and also each disk node can hold a parent node (N*N),in the worst case where each disk can be 
#  placed over the other disk, a situation where all the input disks are utilized for the process.
#> ResultS in worst case space complexity of O(N^2) 