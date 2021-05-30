import numpy as np
def ManualGeometry():
    #array of nodes 1.index 2.position
    Nodes = np.array([[1, 0], 
                      [2, 0.33], 
                      [3, 0.66], 
                      [4, 1]] ) 
       
    #array of elements 1.index 2.index of first nodes 3.index of second node
    Elements = np.array( [[1, 1, 2], 
                       [2, 2, 3], 
                       [3, 3, 4]] )

    #dictionary of edge conditions 1.1 index 1.2 type 1.3 value 2.1 index ...
    EdgeConditions    = [{"Index": 1, "Type":'D', "Value":1}, 
                         {"Index": 4, "Type":'D', "Value":2}]


    return Nodes, Elements, EdgeConditions
