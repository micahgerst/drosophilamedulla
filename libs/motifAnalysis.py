"""Motif Analysis

This script provides a series of functions and basic graphs to aid in the 
analysis of 3 node graph motifs. It provides each of the 13 motifs for 3 node 
graphs and functions to identify motif numbers and spectra of various graphs.

This script requires that `pandas` and `numpy` be installed within the Python 
environment you are running this script in.

This file can also be imported as a module and contains the following 
functions:

    * diGraphDegress - returns an Array containing the in and out degrees of 
                       each node.
    * motifNumber - returns the motif number of a graph of three nodes
    * motifSpectrum - returns a list of all the motifs identified in a graph
    * motifCount - returns how many times a particular motif appears in a 
                   graph.

When imported as a module, this file also contains the following variables:
    * m1 - Motif 1 of a 3 node graph as a Network X DiGraph
    * m2 - Motif 2 of a 3 node graph as a Network X DiGraph
    * m3 - Motif 3 of a 3 node graph as a Network X DiGraph
    * m4 - Motif 4 of a 3 node graph as a Network X DiGraph
    * m5 - Motif 5 of a 3 node graph as a Network X DiGraph
    * m6 - Motif 6 of a 3 node graph as a Network X DiGraph
    * m7 - Motif 7 of a 3 node graph as a Network X DiGraph
    * m8 - Motif 8 of a 3 node graph as a Network X DiGraph
    * m9 - Motif 9 of a 3 node graph as a Network X DiGraph
    * m10 - Motif 10 of a 3 node graph as a Network X DiGraph
    * m11 - Motif 11 of a 3 node graph as a Network X DiGraph
    * m12 - Motif 12 of a 3 node graph as a Network X DiGraph
    * m13 - Motif 13 of a 3 node graph as a Network X DiGraph
    * motifs - a list containing each of the 3 node motifs

"""
import numpy as np
import networkx as nx

def diGraphDegrees(G):
    """
    Calculates the in and out degrees of a graph.
    
    This function takes a NetworkX DiGraph and calculates the in and out 
    degrees by converting the Graph into a NumPy Adjacency Matrix.

    Parameters
    ----------
    G : nx.DiGraph

    Returns
    -------
    degreeArray : np.array 
        an array containing the node index, in degree, and out degree.
    """
    adjMatrix = nx.to_numpy_array(G)
    inDegree = np.sum(adjMatrix, axis=1)
    outDegree = np.sum(adjMatrix, axis=0)
    sideLength = np.size(adjMatrix, axis=0)
    degreeArray = np.zeros([3, sideLength])
    for i in range(sideLength):
            degreeArray[0][i] = i
            degreeArray[1][i] = inDegree[i]
            degreeArray[2][i] = outDegree[i]
    return degreeArray

"""
m1 to m13 represents the 13 motifs found in 3 node graphs. They have been 
created by adding edges based on the motifs from Fornito, Zalesky and Bullmore.
They are then added to a list called motifs.
"""
m1 = nx.DiGraph()
m1.add_edges_from([(2, 1), (3, 1)]) 
m2 = nx.DiGraph()
m2.add_edges_from([(2, 1), (3, 2)]) 
m3 = nx.DiGraph()
m3.add_edges_from([(2, 1), (2, 3)]) 
m4 = nx.DiGraph()
m4.add_edges_from([(1, 2), (2, 1), (3,1)]) 
m5 = nx.DiGraph()
m5.add_edges_from([(2, 1), (3, 1), (3,2)]) 
m6 = nx.DiGraph()
m6.add_edges_from([(1, 2), (1, 3), (2,1)]) 
m7 = nx.DiGraph()
m7.add_edges_from([(1, 3), (3, 2), (2,1)]) 
m8 = nx.DiGraph()
m8.add_edges_from([(1, 2), (2, 1), (3,1), (3,2)]) 
m9 = nx.DiGraph()
m9.add_edges_from([(1, 2), (2, 1), (3,1), (1,3)]) 
m10 = nx.DiGraph()
m10.add_edges_from([(1, 2), (2, 1), (2,3), (3,1)]) 
m11 = nx.DiGraph()
m11.add_edges_from([(2,1), (2, 3), (3,1), (3,2)]) 
m12 = nx.DiGraph()
m12.add_edges_from([(1, 2), (1, 3), (2,1), (3,1),(3,2)])
m13 = nx.DiGraph()
m13.add_edges_from([(1, 2), (1, 3), (2,1), (2,3),(3,1),(3,2)])
motifs = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13]

def motifNumber(G):
    """
    Finds the motif which a graph matches
    
    This function takes a NetworkX DiGraph with exactly 3 nodes to find which 
    motif, if any, the graph is isomorphic to.
    
    Parameters
    ----------
    G : nx.DiGraph
        must have exactly 3 nodes.

    Returns
    -------
    mNum : int 
        int indicating the motif number of the given graph, not the position 
        within motifs.
    """
  
    mNum = None
    for i in range(len(motifs)):
        checkIso = nx.is_isomorphic(G,motifs[i])
        if checkIso == True:
            mNum = i+1
    return mNum 

# Create a function to identify all 3 node motifs in a graph G
def motifSpectrum(G):
    """
    Finds all the 3 node motifs present in a graph.
    
    This function takes a NetworkX DiGraph of any size. It finds all possible 
    triplets and then iterates over each triplet. If it matches a motif, it 
    adds that number to a list. If it does not match any given motif, it checks
    the next triplet.
    
    Parameters
    ----------
    G : nx.DiGraph

    Returns
    -------
    motifList : list 
        list containing the motif number of each triplet
    """
    motifList = []
    triplets = list(nx.all_triplets(G))
    for i in triplets:
        localGraph = nx.subgraph(G, i)
        localMotif = motifNumber(localGraph)
        if localMotif != None:
            motifList.append(localMotif)
    return motifList


def motifCount(G,num):
    """
    Counts how many times a given motif appears in a graph.
    
    This function takes a NetworkX DiGraph of any size. It finds all possible 
    triplets and then iterates over each triplet. If it matches the specified 
    motif, it increases the counter by one.
    
    Parameters
    ----------
    G : nx.DiGraph
    num: int
        int for the motif number of a given graph, i.e. in range(1,14)

    Returns
    -------
    counter : int 
        number of times motif appears in the graph
    """
    counter=0
    triplets = list(nx.all_triplets(G))
    for i in triplets:
        localGraph = nx.subgraph(G, i)
        if nx.is_isomorphic(localGraph,motifs[num-1]) == True:
            counter+=1
    return counter
