def getDistance(p1,p2):
    d = abs (p2 - p1)
    
    return d

def countSquares(coordinates):
    #set of unique coordinate pairs as tuples
    coordinate_set = set(map(tuple, coordinates))
    #print(coordinate_set)
    count = 0
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            if coordinates[i][0] == coordinates[j][0]: #parallel to y axis 
                dist = getDistance(coordinates[i][1],coordinates[j][1]) 
                #changes in x co-ordinate for i and j
                a = coordinates[i][0] + dist
                b = coordinates[j][0] + dist
                #print(a, coordinates[i][1])
                #print(b, coordinates[j][1])
                if (a, coordinates[i][1]) in coordinate_set and (b, coordinates[j][1]) in coordinate_set:
                    count += 1
    return count
    

coordinates = [ [3,1], [0,0],[3,0],[0,1],[1,1],[1,0],[2,1],[2,0]]                   ###3
#coordinates = [ [2,1],[0,0],[0,1],[2,0],[1,1],[1,0],[3,1],[3,0]]                   ###3
#coordinates = [ [0,0],[0,1],[1,1],[1,0],[2,1],[2,0],[3,1],[3,0],[-1,1],[-1,0]]     ###4
#coordinates = [ [1,1],[1,0],[0,0],[0,1],[-1,1],[-1,0]]                             ###2
#coordinates = [ [0,0],[1,0],[0,-1],[1,-1],[0,-2],[1,-2],[0,-3],[1,-3]]             ###3
#coordinates = [ [0,0],[-1,0],[0,-1],[-1,-1],[0,-2],[-1,-2],[0,-3],[-1,-3]]         ###3
#coordinates = [ [0,0],[-1,0],[0,-1],[-1,-1] ]                                      ###1
countSq = countSquares(coordinates)
print(countSq)

#> The worst case time complexity :  O(N^2)
#> N is the number of coordinates in the input list.
#> The outer For loop runs N times, and the inner For loop also runs N times.
#> Hence making the worst case time complexity O(N^2)


#> The space complexity : O(N)
#> N is the number of coordinates in the input list.
#> The maximum size of this set is N, at most there can be N unique coordinate pairs in the input list. 
#> Therefore, the space complexity of the set is O(N).