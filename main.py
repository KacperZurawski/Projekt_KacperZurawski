import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint
#Custom Funcions
from ManualGeometry import ManualGeometry
from AutomaticGeometry import AutomaticGeometry
from DrawGeometry import DrawGeometry
from MemoryAllocation import MemoryAllocation
from BaseFunctions import BaseFunctions
from Aij import Aij
from PlotResult import PlotResult

if __name__ == '__main__':
    
    c = 0
    f = lambda x: 0*x 
    
    #MANUAL GEOMETRY
    Nodes, Elements, EdgeConditions = ManualGeometry()
    NumberOfNodes = np.shape(Nodes)[0]
   
    
    #AUTOMATIC GEOMETRY
    #XPosStart =  0 
    #XPosEnd =  1
    #NumberOfNodes = 4
    #Nodes, Elements, EdgeConditions = AutomaticGeometry(XPosStart,XPosEnd,NumberOfNodes);

    DrawGeometry(Nodes, Elements, EdgeConditions)

    A,b = MemoryAllocation(NumberOfNodes)
    

    BaseFunctionDegree = 1
    phi, dphi = BaseFunctions(BaseFunctionDegree)

    #Checking if base functions are properly defined
     
    plt.figure()
    xx = np.linspace(-1,1, 2) 
    plt.plot(xx, phi[0](xx), 'r' )
    plt.plot(xx, phi[1](xx), 'g' )
    plt.plot(xx, dphi[0](xx), 'b' )
    plt.plot(xx, dphi[1](xx), 'c' )
    

    
    NumberOfElements = np.shape(Elements)[0]
    
    for CurrentElement in np.arange(0, NumberOfElements ):
              
        FirstNode = Elements[CurrentElement,1]     # indeks wezla poczatkowego elemntu ee
        SecondNode = Elements[CurrentElement,2]     # indeks wezla koncowego elemntu ee
        NodeGlobalIndexes = np.array([FirstNode, SecondNode ])
    
        XPosStart = Nodes[ FirstNode-1 ,1]
        XPosEnd = Nodes[ SecondNode-1 ,1]
    
    
        Ml = np.zeros( [BaseFunctionDegree+1, BaseFunctionDegree+1] )
        
        J = (XPosEnd-XPosStart)/2
        
        m = 0; n = 0 ;
        Ml[m,n] = J * spint.quad( Aij(dphi[m], dphi[n], c, phi[m],phi[n]), 0, 1)[0]
        
        m = 0; n = 1 ;
        Ml[m,n] = J * spint.quad( Aij(dphi[m], dphi[n], c, phi[m],phi[n]), 0, 1)[0]
        
        m = 1; n = 0 ;
        Ml[m,n] = J * spint.quad( Aij(dphi[m], dphi[n], c, phi[m],phi[n]), 0, 1)[0]
        
        m = 1; n = 1 ;
        Ml[m,n] = J * spint.quad( Aij(dphi[m], dphi[n], c, phi[m],phi[n]), 0, 1)[0]
                

        A[np.ix_(NodeGlobalIndexes-1, NodeGlobalIndexes-1  ) ] =  \
            A[np.ix_(NodeGlobalIndexes-1, NodeGlobalIndexes-1  ) ] + Ml
  

    
    # Edge Conditions
    if EdgeConditions[0]['Type'] == 'D':
        ind_wezla = EdgeConditions[0]['Index']
        wart_war_brzeg = EdgeConditions[0]['Value']
        
        iwp = ind_wezla - 1
        
        WZMACNIACZ = 10**14
        
        b[iwp] = A[iwp,iwp]*WZMACNIACZ*wart_war_brzeg
        A[iwp, iwp] = A[iwp,iwp]*WZMACNIACZ
        
        
    if EdgeConditions[1]['Type'] == 'D':
        ind_wezla = EdgeConditions[1]['Index']
        wart_war_brzeg = EdgeConditions[1]['Value']
        
        iwp = ind_wezla - 1
        
        WZMACNIACZ = 10**14
        
        b[iwp] = A[iwp,iwp]*WZMACNIACZ*wart_war_brzeg
        A[iwp, iwp] = A[iwp,iwp]*WZMACNIACZ        
  
    u = np.linalg.solve(A,b)
    
    PlotResult(Nodes, u)
    
    
    
    
    