import numpy as np
import matplotlib.pyplot as plt

def DrawGeometry(Nodes, Elements, EdgeConditions):
    plt.figure()
    plt.plot(Nodes[:,1], np.zeros( (np.shape(Nodes)[0], 1) ), '-b|' )
       
    NumberOfNodes = np.shape(Nodes)[0]
    NumberOfElements = np.shape(Elements)[0]

    for CurrentNode in np.arange(0,NumberOfNodes):
        Index = Nodes[CurrentNode,0]
        XPos = Nodes[CurrentNode,1]
        plt.text(XPos, 0.01, str( int(Index) ), c="b")
        plt.text(XPos-0.035, -0.01, str(round(XPos,3)))
     
    for CurrentElement in np.arange(0,NumberOfElements):
        FirstNode = Elements[CurrentElement,1]
        SecondNode = Elements[CurrentElement,2]
        XPos = (Nodes[FirstNode-1,1] + Nodes[SecondNode-1,1] ) / 2  
        plt.text(XPos, 0.01, str(CurrentElement+1), c="r")
        
    plt.text(Nodes[0,1]-0.035, -0.02, str(EdgeConditions[0]['Type']) + " " + str(EdgeConditions[0]['Value']))
    plt.text(Nodes[NumberOfNodes-1,1]-0.035, -0.02, str(EdgeConditions[1]['Type']) + " " + str(EdgeConditions[1]['Value']))
    
    plt.show()
    
