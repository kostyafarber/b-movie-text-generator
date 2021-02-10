import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_pickle('test.pkl')

# bar plot of movie genres
df.genres.explode().value_counts().plot(kind='barh')

# average run time
df.runtimes.explode().astype('float').mean()

