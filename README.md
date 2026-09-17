<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">epidemiology_proj</h3>

  <p align="center">
    Armaan Tickoo* &middot; Isha Marla*
    <br />
    <sub>*Equal contribution</sub>
    <br />
    <br />
    This project compares shopper strategies for reducing disease spread across a network of households, using recovered immunity to lower the final size of an outbreak. It uses a discrete-time SEIR simulation with various strategies including rotating, designated, and adaptive, noting the significant differences in total infected population.
    <br />
    <a href="https://github.com/ishamarla17/epidemicproj"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ishamarla17/epidemicproj/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/ishamarla17/epidemicproj/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project compares shopper strategies for reducing disease spread across a network of households, using recovered immunity to lower the final size of an outbreak. It uses a discrete-time SEIR simulation with various strategies including rotating, designated, and adaptive, noting the significant differences in total infected population.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]
* [![NumPy][NumPy.org]][NumPy-url]
* [![SymPy][SymPy.org]][SymPy-url]
* [![Matplotlib][Matplotlib.org]][Matplotlib-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

* Python 3.x
* pip
  ```sh
  pip install --upgrade pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ishamarla17/epidemicproj.git
   ```
2. Navigate into the project directory
   ```sh
   cd epidemicproj
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the main simulation with:
```sh
python BaseProject.py
```

This runs the discrete-time SEIR simulation comparing shopper strategies (designated, rotate, random, adaptive, and adaptive smart) across a network of households. It outputs a 50-trial, 20-household total population infected percentage. To increase the household count, `beta_store` must be adjusted accordingly, otherwise the output will be inaccurate. To change the number of trials, edit the `trials` variable near the bottom of the code.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Contributors

<a href="https://github.com/ishamarla17/epidemicproj/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ishamarla17/epidemicproj" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Co-authors (equal contribution):

* Armaan Tickoo - [@armaantickoo](https://github.com/armaantickoo) - armaan@tickoo.net
* Isha Marla - [@ishamarla17](https://github.com/ishamarla17) - ishamarla17@gmail.com

Project Link: [https://github.com/ishamarla17/epidemicproj](https://github.com/ishamarla17/epidemicproj)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ishamarla17/epidemicproj.svg?style=for-the-badge
[contributors-url]: https://github.com/ishamarla17/epidemicproj/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ishamarla17/epidemicproj.svg?style=for-the-badge
[forks-url]: https://github.com/ishamarla17/epidemicproj/network/members
[stars-shield]: https://img.shields.io/github/stars/ishamarla17/epidemicproj.svg?style=for-the-badge
[stars-url]: https://github.com/ishamarla17/epidemicproj/stargazers
[issues-shield]: https://img.shields.io/github/issues/ishamarla17/epidemicproj.svg?style=for-the-badge
[issues-url]: https://github.com/ishamarla17/epidemicproj/issues
[license-shield]: https://img.shields.io/github/license/ishamarla17/epidemicproj.svg?style=for-the-badge
[license-url]: https://github.com/ishamarla17/epidemicproj/blob/master/LICENSE.txt
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[NumPy.org]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[SymPy.org]: https://img.shields.io/badge/SymPy-3B5526?style=for-the-badge&logo=sympy&logoColor=white
[SymPy-url]: https://www.sympy.org/
[Matplotlib.org]: https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge
[Matplotlib-url]: https://matplotlib.org/
