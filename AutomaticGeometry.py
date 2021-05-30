import numpy as np

def AutomaticGeometry(XPosStart,XPosEnd,NumberOfNodes):

    
    #array of nodes indexes
    Indexes = np.arange(1,NumberOfNodes+1)
    #array of nodes positions
    XPositions = np.linspace(XPosStart,XPosEnd,NumberOfNodes) ;        
    #array of nodes 1.index 2.position
    Nodes = (np.vstack( (Indexes.T, XPositions.T) )).T

    #array of first nodes indexes
    FirstNodesArray = np.arange(1,NumberOfNodes)
    #array of second nodes indexes
    SecondNodesArray = np.arange(2,NumberOfNodes+1)
    #array of elements 1.index 2.index of first nodes 3.index of second node
    Elements = (np.block( [[Indexes[0:len(Indexes)-1]], [FirstNodesArray], [SecondNodesArray] ] ) ).T
    EdgeConditions  = [{"Index": 1, "Type":'D', "Value":1},
                       {"Index": NumberOfNodes, "Type":'D', "Value":2}]
    return Nodes, Elements,EdgeConditions
