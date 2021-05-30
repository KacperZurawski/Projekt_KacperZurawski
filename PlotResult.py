import matplotlib.pyplot as plt

def PlotResult(Nodes, u):

    NodeXPositions = Nodes[:,1]
     
    plt.figure()
    plt.plot(NodeXPositions, u, '*-')