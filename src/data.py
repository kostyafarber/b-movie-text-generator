

# import trash list
from text_preprocessing import trash_list

# IMDbPY API imports
import imdb
from imdb import helpers
from imdb import IMDb
import pandas as pd

# instantiate IMDb class
ia = IMDb()

# search for movie from each element in trash list
movie_test = [ia.search_movie(x) for x in trash_list]

# pick first object for each movie (seems to match movies well the first time)
movies_final = [x[0] for x in movie_test if len(x) != 0]

# check available info sets (use this for reference if I want to grab more data).
info = ia.get_movie_infoset()

# loop to update movie data with relevant data
for x in movies_final:
    ia.update(x, info=['main', 'keywords', 'critic reviews', 'quotes', 'plot'])

# create DataFrame with move data.
df = pd.DataFrame.from_dict(movies.data for movies in movies_final)

# helper functions to format person objects in readable format, for cast and general objects.
myPrint_cast = imdb.helpers.makeObject2Txt(personTxt=u'%(name)s as %(currentRole)s')
myPrint = imdb.helpers.makeObject2Txt(personTxt=u'%(name)s')

# extract columns to reformat
columns_reformat = []

for x in df.columns:
    # all the rows that have entries as lists
    for y in df[x]:
        # check if row is a list
        try:
            if isinstance(y, list):
                # if first entry a Person or Company Object append to column list
                if isinstance(y[0], (imdb.Person.Person, imdb.Company.Company)):
                    columns_reformat.append(x)
        # catch index errors and continue.
        except IndexError:
            continue

# Multiple column names extract unique names and re-assign to list.
columns_reformat = list(set(columns_reformat))

# reformat IMDbPY objects as pretty strings
for x in columns_reformat:

    if x != "cast":
        df[x] = df[x].apply(lambda l: myPrint(l))

    # apply different string formatter for cast to have in format (actor as role)
    else:
        df[x] = df[x].apply(lambda l: myPrint_cast(l))

# save as pickle for quick load and import.
df.to_pickle('trash_df.pkl')
