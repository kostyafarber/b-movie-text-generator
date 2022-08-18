import streamlit as st
import pandas as pd
import os
from utils import generate_wordcloud
from movie import Movie
from generator import Generator

# setup
data_path = '/app/bad-movies/src/app/data/processed/trash_df.pkl'
images_path = 'assets/images/7black.png'

df_bad = pd.read_pickle(data_path)
df_bad.dropna()
st.set_page_config(page_title='Zoltare', page_icon='random')

# grab movie attributes
movies = Movie(df_bad)
title = movies.get_title()
year = movies.get_year()
rating = movies.get_rating()
summary = movies.get_summary()

# keywords
keywords = movies.get_keywords()
keywords_text = movies.generate_keyword_str()



#prompt = 'Write a movie plot based on these keywords: {}'.format(keywords_df[0:1500])

#st.title('\U0001F916')
#st.image("../assets/images/gba_animation.gif")
st.image(os.path.join(images_path, '7black.png'))
st.title('If a robot was a writer of b-movies...')

# selecting the prompt for the generator
prompt_options = ['movie plot', 'angry email', 'cover letter', 'advertisement']
selected_prompt = st.selectbox(label='What kind of nonsense do you want?', options=prompt_options)
text = f'Write a {selected_prompt} based on these keywords: {keywords_text}'

# generate text completion based on prompt
generator = Generator()
generated_text = generator.generate_text(text)
st.markdown(generated_text)
st.markdown('<br>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.write("")

with col2:
    if st.button("Robot, generate more b-movie nonsense please!"):
        random_row = movies.random_row

with col3:
    st.write("")


desc = '''
No, I'm not talking about the awesome podcast 
[How Did This Get Made ](https://en.wikipedia.org/wiki/How_Did_This_Get_Made%3F).

One of my fond memories of a bygone era was visiting the local 
video store, the now ancient __Video Ezy__, to pick up a movie 
with my friends. We would go to each others houses and 
have a movie marathon and watch all types of films. 
Some good, some bad.

We started watching all the bad movies we could find, because they were
often the __funniest__. We recorded each movie in a list, and 
this project is based on those movies.

# Technologies 
- [`cinemagoer`](https://cinemagoer.github.io/) used for obtaining IMDb data.
- [`openai/gpt-3`](https://openai.com/blog/gpt-3-apps/) is for generating the hilariously funny text.

Check out the source for this app [here](https://github.com/kostyafarber/bad-movies).
'''

with st.sidebar:
    st.title('How Did This Get Made?')
    st.markdown(desc, unsafe_allow_html=True)

    st.title("Original Awful Movie \U0001F3AC")
    st.header(f'{title} ({year}) \U0001F31F {rating}')
    
    # sometimes there isn't a summary on IMDb
    if isinstance(summary, str):
        st.write(summary)
    else:
        st.write("Cannot find summary, it must be that bad.")

    # wordcloud 
    fig = generate_wordcloud(keywords_text)
    st.pyplot(fig)
    st.caption(f"keywords from IMDb for the movie: {title}")
