import numpy as np

def MemoryAllocation(NumberOfNodes):
    A = np.zeros([NumberOfNodes,NumberOfNodes])
    b = np.zeros([NumberOfNodes,1])

    return A,b
