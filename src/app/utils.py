from wordcloud import WordCloud
import os
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    """
    filler
    """

    font_path = os.path.abspath('src/app/fonts/TestFoundersGrotesk-Bold.otf')

    wc = WordCloud(
                    width=2000, 
                    height=1000, 
                    font_path=font_path, 
                    background_color="white", 
                    max_words=500).generate(text)

    # change the value to black
    def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
        return("hsl(0,100%, 1%)")

    wc.recolor(color_func=black_color_func)

    # Display the generated image:
    fig, ax = plt.subplots()
    plt.imshow(wc)
    plt.axis("off")

    return fig