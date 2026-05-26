Drosophilia Analysis
*** README version 1.0 ***
-----------------------------------------------------------------------------------
*** About ***

This library provides the required files and final documentation for an exploration
of the Drosophilia connectome. The main project, ME(R)_analysis.py, provides images
and data for the analysis of the medulla region of the Drosophilia connectome.


*** Instructions ***
1. Download the zip file.
2. Unzip it into a folder which your ODE can access.
3. Open library in an ODE of your choice (we used Spyder!).
4. Run ME(R)_analysis.py.

*** Dependencies ***
This library requires that the latest version of pandas, matplotlib, and networkx
are installed.

*** Packages ***
It comes with three packages pre-installed in /libs:
* CSV_filtering.py - Filters drosophilia data for a region of interest
* motifAnalysis.py - Package used to analyse motif isomorphisms
* normalisingMotifs.py - Creates random graphs to generate a null model.

Each package has its own documentation available.

*** Data ***

Associated with these packages is pre-existing data in /libs/data:
* traced-roi-connections.csv
* ME(R)_data.csv
* m3_random_graphs.csv

In the case ME(R)_data.csv or m3_random_graphs.csv is missing, run both 
CSV_filtering.py and normalisingMotifs.py to generate the data. If 
traced-roi-connections.csv is missing, please download it using the link in
the resources.

*** Figures ***
Figures generated using this code are exported to /figures.

*** Publications:
The final report of this project is saved as PDF in the main environment.
It can be accessed by opening Drosophilia_Graph_Motifs_in_the_Medulla.pdf.

*** Resources ***
More information on NetworkX can be found here:
https://networkx.org/documentation/stable/reference/index.html
More information on pandas can be found here:
https://pandas.pydata.org/docs/
More information on matplotlib can be found here:
https://matplotlib.org/stable/index.html
The Drosophilia melanogaster data can be downloaded here: 
https://dvid.io/blog/release-v1.2/#downloads
