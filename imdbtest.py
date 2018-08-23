import pandas as pd

pathdataset="D:\\machinelearning\\IMDB-Movie-Data.csv"
metadata=pd.read_csv(pathdataset)
print metadata
#print metadata.describe("Metascore")
print metadata.head(3)
#print metadata['Metascore']
meanVotes=metadata['Rating'].mean()
print meanVotes
#grouped= metadata.groupby(metadata['Votes']>meanVotes)
print list(metadata.columns.values)
#for name,group in grouped:
#	print name
#	print group
m = metadata['Votes'].quantile(0.90)
print(m)
q_movies = metadata.copy().loc[metadata['Votes'] >= m]
print q_movies.shape

def weighted_rating(x, m=m, C=C):
    v = x['Votes']
    R = x['Rating']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)
	
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)

print q_movies[['title', 'vote_count', 'vote_average', 'score']].head(15)