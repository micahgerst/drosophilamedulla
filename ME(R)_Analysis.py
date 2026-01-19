"""ME(R) Analysis

This script is the module which makes full use of the motifAnalysis module
and the data files created with the `CSV_filtering` and `normalisingMotifs`
packages. It creates graphs and histograms which are explorted to `/figures`
and returns some key values for analysis in the final report.

This script requires that `NetworkX`,`Pandas`, and `MatPlotLib` are installed 
in the coding environment.

This script depends on `motifAnalysis`, `normalisingMotifs`, and 
`CSV_filtering` packages being installed in `/libs`. 
`traced-roi-connections.csv` should come preinstalled in `/libs/data`. If 
`m3_random_motifs.csv` isn't present in that directory, run `normalisingMotifs`.
If `ME(R)_data.csv` isn't present in that directory, run `CSV_filtering`
"""
import networkx as nx
import pandas as pd
import motifAnalysis as ma
import matplotlib.pyplot as plt

"""
This section imports the ME(R) data and converts it to a NetworkX DiGraph
for use throughout the programme. This graph is then drawn and exported. It is
used in section 2.1 of the report.
"""
data = pd.read_csv('libs/data/ME(R)_data.csv')
circuitGraph = nx.from_pandas_edgelist(data, "bodyId_pre", "bodyId_post", 
                                       "weight",create_using=nx.DiGraph())
circuitGraph = nx.convert_node_labels_to_integers(circuitGraph)


plt.figure(figsize=(16, 12))
im = nx.draw_networkx(circuitGraph, with_labels=True, node_color='#88CCEE', 
                      font_weight='bold', pos=nx.circular_layout(circuitGraph))
plt.title("Graph of the Drosophilia Connectome in the Medulla", fontsize=30)
plt.savefig("figures/medulla_graph")


"""
This section creates the motif frequency spectrum for the ME(R) data using the
motifSpectrum function from the `motifAnalysis` package. The histogram is
exported and used in section 2.2 of the report.
"""
motifList = ma.motifSpectrum(circuitGraph)

plt.figure(figsize=(8, 4))
values, bins, bars = plt.hist(motifList, bins=13, range=(1,14),
                              facecolor = '#004488', edgecolor='black', 
                              linewidth=0.5)
plt.title("Distribution of Isomorphic 3 Node Motifs in the Drosophilia Medulla")
plt.xlabel("Motif Number")
plt.ylabel("Number of Isomorphisms")
plt.bar_label(bars, fontsize=15, color='navy')
plt.margins(x=0.01, y=0.1)
plt.xticks(ticks=[1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5], 
           labels=range(1,14))
plt.savefig("figures/medulla_isomorphisms")


"""
This section prepares for the generation of a null model by finding the ME(R)
graph's characteristics, including number of nodes, edges, and its density. 
These are used to describe the graph in section 2.1 and then to generate the
random graphs in section 2.2, 2.3, and the appendix.
"""
cGDensity = nx.density(circuitGraph)
cGSize = nx.number_of_nodes(circuitGraph)
cGEdges = nx.number_of_edges(circuitGraph)


"""
This section generates the random graph referred to in section 2.2 and the 
appendix. It and its motif frequency spectrum is drawn and exported for use in 
the appendix.
"""
randomGraph = nx.gnp_random_graph(cGSize,cGDensity, seed=238748, 
                                  directed= True)
randomGraph = nx.convert_node_labels_to_integers(randomGraph)

plt.figure(figsize=(16, 12))
im = nx.draw_networkx(randomGraph, with_labels=True, node_color='#88CCEE', 
                      font_weight='bold', pos=nx.circular_layout(randomGraph))
plt.title("Random Graph", fontsize=30)
plt.savefig("figures/random_graph")

motifListRand = ma.motifSpectrum(randomGraph)
plt.figure(figsize=(8, 4))
values, bins, bars = plt.hist(motifListRand, bins=13, range=(1,14),
                              facecolor='#DDAA33', edgecolor='black', 
                              linewidth=0.5)
plt.title("Distribution of Isomorphic 3 Node Motifs in a Random Graph")
plt.xlabel("Motif Number")
plt.ylabel("Number of Isomorphisms")
plt.bar_label(bars, fontsize=15, color='navy')
plt.margins(x=0.01, y=0.1)
plt.xticks(ticks=[1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5], 
           labels=range(1,14))
plt.savefig("figures/rand_isomorphisms")


"""
This section takes the ME(R) and random motif frequency spectra and 
superimposes them on one another. The final image is exported and used in 
section 2.2 of the final report.
"""
plt.figure(figsize=(8, 4))
plt.hist(motifList, bins=13, range=(1,14),facecolor = '#004488', 
         edgecolor='black', linewidth=0.5, alpha=0.5)
plt.hist(motifListRand, bins=13, range=(1,14), facecolor = '#DDAA33', 
         edgecolor='black', linewidth=0.5, alpha=0.5)
plt.title("Distribution of Isomorphic 3 Node Motifs")
plt.xlabel("Motif Number")
plt.ylabel("Number of Isomorphisms")
plt.margins(x=0.01, y=0.1)
plt.xticks(ticks=[1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5], 
           labels=range(1,14))
plt.legend(["Drosophilia Medulla Connectome", "Random Graph"])
plt.savefig("figures/medulla_and_rand")


"""
Based on the analysis from section 2.2, this section identifies whether the
occurrence of motif 3 is significant or not. It reads the data from
`lib/data/m3_random_motifs.csv` as created by the `normalisingMotifs` package.
These results are drawn onto a histogram approximating the distribution of 
motif 3 in similar graphs exported to a figure used in section 2.3 of the 
final report. 
"""
m3Total = ma.motifCount(circuitGraph,3)
lineLabel = 'x =' + str(m3Total)
m3Counts = pd.read_csv('libs/data/m3_random_motifs.csv', usecols=['motifCount'])

plt.figure(figsize=(8, 4))
values, bins, bars = plt.hist(m3Counts, bins=range(40,150,10), 
                              facecolor = '#BB5566', edgecolor='black', 
                              linewidth=0.5)
plt.title("Distribution of Graphs Isomorphic to M3 in Random Graphs (n=100)")
plt.xlabel("Number of M3 Isomorphic Subgraphs")
plt.ylabel("Number of Random Graphs")
plt.bar_label(bars, fontsize=15, color='navy')
plt.margins(x=0.01, y=0.1)
plt.xticks(range(40,150,10))
plt.axvline(x = m3Total, color = 'blue')
plt.text(130,20, lineLabel)
plt.savefig("figures/normalM3")

