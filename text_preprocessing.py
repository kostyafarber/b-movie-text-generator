import pandas as pd
import re

with open("trash-movie-list.txt", ) as file:
    # read txt file, convert to list
    lines = [x.strip() for x in file.readlines()]

    # replace all numberings and everything in front the dashes
    pattern = '\-.*|^\d*.'
    replace = ""

    # store cleaned titles as specified by regex in a new list
    trash_list = [re.sub(pattern, replace, x).strip() for x in lines]

# store list in dataframe
df_movies = pd.DataFrame(trash_list, columns=['Titles'])

print(df_movies.head())
