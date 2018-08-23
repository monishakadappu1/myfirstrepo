import pandas as pd

def recommenMovie(movieTitle):
	pathdataset="D:\\machinelearning\\IMDB-Movie-Data.csv"
	metadata=pd.read_csv(pathdataset)
	print "The cast of the movie you se;lected is "
	grouped=metadata.groupby('Title')
	i=1
	for name,group in grouped:
		print i
		print "title of the movie " + name
		print group['Title']
		a= group['Actors']
		
		i+=1
	print grouped['Title','Actors'].get_group(movieTitle)
	#print grouped['Title'].agg('Actors')
print "Enter the movie you want to watch"
movie=raw_input()
recommenMovie(movie)

