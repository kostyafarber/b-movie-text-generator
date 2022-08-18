from random import randint
import pandas as pd

class Movie():
    """
    A class that is used to generate movie attributes.
    """
    def __init__(self, data: pd.DataFrame()) -> None:
        self.data = data
        self.random_row = self._generate_random_row()

    def _generate_random_row(self) -> int:
        """Generates a random integer from the range of 0 to n (n is #rows in dataframe)

        Returns:
            returns an int
        """
        return randint(0, self.data.shape[0])

    def get_title(self) -> str:
        """Used to get the title of the movie

        Returns:
            returns a str
        """
        keyword = self.data['title'][self.random_row]
        return keyword

    def get_summary(self) -> str:
        """Used to provide the summary of the plot

        Returns:
            returns a str
        """
        title = self.data['plot outline'][self.random_row]
        return title

    def get_year(self) -> str:
        """Used to get the year of when the movie was made

        Returns:
            returns an int
        """
        
        try:
            year = int(self.data['year'][self.random_row])            
            return year

        except ValueError:
            return "Year Unknown"


    def get_rating(self) -> str:
        """Used to get the rating of the movie per IMDb

        Returns:
            returns a float
        """
        rating = self.data['rating'][self.random_row]
        return rating

    def get_keywords(self) -> str:
        """Used to grab all keywords associated with the movie per IMDb

        Returns:
            reutrns a list of strings
        """
        keywords = self.data['keywords'][self.random_row]
        return keywords

    def generate_keyword_str(self) -> str:
        """Used to turn a list of keyword strings into a one long string

        Returns:
            a str
        """
        return " ".join(self.get_keywords())



