"""CSV ROI Filtering

This script imports the Drosophilia connectome and counts how many connections 
are in each ROI. In this example, ME(R) is selected and exported to
CSV.

This script requires that `pandas` and `traces-roi-connections.csv` be 
installed within the Python environment you are running this script in.

"""
import pandas as pd

data = pd.read_csv("data/traced-roi-connections.csv")

#%%
grouped = data.groupby(["roi"], sort=False).count()


#%%
roiData = data.loc[lambda df: df['roi'] == 'ME(R)', :]

#%%
roiData.to_csv('data/ME(R)_data.csv')