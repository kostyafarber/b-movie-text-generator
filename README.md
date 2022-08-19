<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://kostyafarber.github.io"/>
    <img src="src/assets/images/puzzle.png" alt="Logo" width="40" height="40">
  </a>

<h3 align="center">B-Movie Text Generator</h3>

  <p align="center">
    This project scrapes car prices every morning using AWS Lambda and stores them in a DynamoDB table. I used this to help me sell my car before I moved to London from Sydney.
    <br />
    <a href="https://github.com/kostyafarber/car-sales"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kostyafarber/car-sales">View Demo</a>
    ·
    <a href="https://github.com/kostyafarber/car-sales/issues">Report Bug</a>
    ·
    <a href="https://github.com/kostyafarber/car-sales/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://nextjs.org/)
* [Streamlit](https://reactjs.org/)
* [OpenAI](https://vuejs.org/)
* [Cinemagoer](https://vuejs.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## How Did This Get Made?
Check out the sidebar on the app to find out more 😏

<p align="center">
  <img src="https://media.giphy.com/media/bbWHn9uZc0dxsWTm5E/giphy.gif" width='800'>
</p>

### Prerequisites

Make sure you have `docker` installed. You can find instructions on their [website](https://docs.docker.com/get-docker/).  

### Installation

_To instal the project locally follow the instructions below._

1. Get a free API Key at [https://openai.com/](https://openai.com/)

2. Clone the repo
   ```sh
   git clone git@github.com:kostyafarber/bad-movies.git
   ```

3. Enter your API key in `src/.streamlit/.secrets.toml`
   ```toml
   OPENAI_API_KEY = 'ENTER YOUR API';
   ```

4. Make sure you are at the root

  ```project
├── Dockerfile
├── README.md
├── docker-compose.yml
├── notebooks
│   └── bad-movies-eda.ipynb
├── requirements.txt
└── src
    ├── app
    │   ├── data.py
    │   ├── generator.py
    │   ├── main.py
    │   ├── movie.py
    │   ├── text_preprocessing.py
    │   └── utils.py
    ├── assets
    │   └── images
    │       ├── 7black.png
    │       ├── puzzle.png
    │       └── zoltare-laptop.gif
    ├── data
    │   ├── processed
    │   │   └── trash_df.pkl
    │   └── raw
    │       ├── notes.txt
    │       ├── trash-movie-list.txt
    │       └── wiki_movie_plots_deduped.csv
    └── fonts
        └── TestFoundersGrotesk-Bold.otf
  ```


To run the the app, build and run the container with `docker-compose`

  ```sh
  docker-compose -f docker-compose.yml up --build               
  ```

5. Navigate to `localhost:8501` in your web browser and enjoy the hilarity!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Email: kostya.farber@gmail.com

Project Link: [https://github.com/kostyafarber/car-sales](https://github.com/kostyafarber/car-sales)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Thanks to this [article](https://towardsdatascience.com/how-to-make-word-clouds-in-python-that-dont-suck-86518cdcb61f) on helping me improve the vanilla Python wordclouds for this project! Good stuff.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kostyafarber/car-sales.svg?style=for-the-badge
[contributors-url]: https://github.com/kostyafarber/car-sales/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kostyafarber/car-sales.svg?style=for-the-badge
[forks-url]: https://github.com/kostyafarber/car-sales/network/members
[stars-shield]: https://img.shields.io/github/stars/kostyafarber/car-sales.svg?style=for-the-badge
[stars-url]: https://github.com/kostyafarber/car-sales/stargazers
[issues-shield]: https://img.shields.io/github/issues/kostyafarber/car-sales.svg?style=for-the-badge
[issues-url]: https://github.com/kostyafarber/car-sales/issues
[license-shield]: https://img.shields.io/github/license/kostyafarber/car-sales.svg?style=for-the-badge
[license-url]: https://github.com/kostyafarber/car-sales/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kostyafarber
[product-screenshot]: src/assets/images/zoltare-laptop.gif
