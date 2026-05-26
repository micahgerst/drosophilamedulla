"""Normalise Motif Counts

This script generates random graphs and calculates how many times a particular 
3 node motif appears in the random graph. These are added to a list and 
exported to a CSV file so it can be read into other programmes.

This script requires that `pandas` `NetworkX`and `motifAnalysis` be installed 
within the Python environment you are running this script in.`ME(R)_data`
should be a folder called data, which can be done by running the 
`CSV_filtering` module.
"""

import networkx as nx
import pandas as pd
import motifAnalysis as ma

data = pd.read_csv('data/ME(R)_data.csv')
circuitGraph = nx.from_pandas_edgelist(data, "bodyId_pre", "bodyId_post", 
                                       "weight",create_using=nx.DiGraph())

cGDensity = nx.density(circuitGraph)
cGSize = nx.number_of_nodes(circuitGraph)

#%% 
m3Norm =[]
for i in range(100):
    testGraph = nx.fast_gnp_random_graph(cGSize,cGDensity, directed= True)
    testCount = ma.motifCount(testGraph,3)
    m3Norm.append(testCount)
    
#%%
m3NormDF = pd.DataFrame(m3Norm, columns=['motifCount'])
m3NormDF.to_csv('data/m3_random_motifs.csv')