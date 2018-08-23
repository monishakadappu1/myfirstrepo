import pandas as pd

pathdataset="D:\\machinelearning\\IMDB-Movie-Data.csv"
metadata=pd.read_csv(pathdataset)
print metadata['Director']
#DirList=metadata.copy().loc[metadata['Director','Luke Greenfield']]
#print DirList
grouped = metadata.groupby('Director')
print grouped['Title','Director'].get_group('James Gunn')
#print movies['Title','Director']