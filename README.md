<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
    <a href="https://github.com/mauriciohc02/Snells-Law_Calculator">
        <img src="images/app_icon.png" alt="Logo" width="80" height="80">
    </a>
    <h3 align="center">Snells-Law_Calculator</h3>
    <p align="center">
        An awesome Calculator to undersand how Snell's Law works!
        <br />
        <a href="https://github.com/mauriciohc02/Snells-Law_Calculator"><strong>Explore the docs »</strong></a>
        <br />
        <br />
        <a href="https://github.com/mauriciohc02/Snells-Law_Calculator">View Demo</a>
        ·
        <a href="https://github.com/mauriciohc02/Snells-Law_Calculator/issues">Report Bug</a>
        ·
        <a href="https://github.com/mauriciohc02/Snells-Law_Calculator/issues">Request Feature</a>
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
        <li><a href="#license">License</a></li>
    </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">
    <a href="https://github.com/mauriciohc02/Snells-Law_Calculator/blob/main/images/screenshot.png">
        <img src="https://raw.githubusercontent.com/mauriciohc02/Snells-Law_Calculator/main/images/screenshot.png" alt="Logo" width="500" height="537">
    </a>
</div>

When light travels from one medium to another, it bends or refracts. The Snells-Law_Calculator lets you explore this topic in detail and understand the principles of refraction.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Pyqt5][Pyqt5]][Pyqt5-url]
* [![Numpy][Numpy]][Numpy-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Docker][Docker]][DockerImage-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Before you begin, it is good to know that there are two different ways to deploy the application:

1.  **Traditional Method:** Installing every single python library and package in order to run the app successfully.

2.  **Docker Method:** Pulling the docker image in order to run the app successfully.

So, to get a local copy up and running the project follow these simple steps.


### Prerequisites

* First of all, ensure you have met one of the following requirements, depending on the method already chosen:
    - [Python][Python-url]
    - [Docker][Docker-url]


### Installation

1. For both deploy methods **clone this repository**.
    ```bash
    git clone https://github.com/mauriciohc02/Snells-Law_Calculator.git
    ```

2.  Get into the **project directory**.
    ```bash
    cd Snells-Law_Calculator
    ```

3.  If you chose the **Traditional Method** run the first command to install the modules or packages, otherwise for the **Docker Method** just pull the docker image as shown in the last command.
    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    docker pull mauriciohc/snells-law
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1.  **Traditional Method:** Run the python command below:
    ```bash
    python3 main.py
    ```

2.  **Docker Method:** To deploy the project, you have to run some commands and the [`docker-compose.yml`][Compose-url], but with the [`run.sh`][Script-url] script you can run it with just the following command.
    ```bash
    bash run.sh
    ```

**Note:** When using the **Docker Method**, the container creates `plots/` directory, if you want to remove it run the command below:
```bash
sudo rm -r plots/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE.md`][license-url] for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/mauriciohc02/Snells-Law_Calculator.svg?style=for-the-badge
[contributors-url]: https://github.com/mauriciohc02/Snells-Law_Calculator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mauriciohc02/Snells-Law_Calculator.svg?style=for-the-badge
[forks-url]: https://github.com/mauriciohc02/Snells-Law_Calculator/network/members
[stars-shield]: https://img.shields.io/github/stars/mauriciohc02/Snells-Law_Calculator.svg?style=for-the-badge
[stars-url]: https://github.com/mauriciohc02/Snells-Law_Calculator/stargazers
[issues-shield]: https://img.shields.io/github/issues/mauriciohc02/Snells-Law_Calculator.svg?style=for-the-badge
[issues-url]: https://github.com/mauriciohc02/Snells-Law_Calculator/issues
[license-shield]: https://img.shields.io/github/license/mauriciohc02/Snells-Law_Calculator.svg?style=for-the-badge
[license-url]: https://github.com/mauriciohc02/Snells-Law_Calculator/blob/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mauricio-hernandez-cepeda

[Python]: https://img.shields.io/badge/PYTHON-V3.10-blue?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/
[Pyqt5]: https://img.shields.io/badge/PYQT5-V5.15.7-blue?style=for-the-badge&logo=qt
[Pyqt5-url]: https://pypi.org/project/PyQt5/
[Numpy]: https://img.shields.io/badge/NUMPY-V1.23.4-blue?style=for-the-badge&logo=numpy&logoColor=lightblue
[Numpy-url]: https://numpy.org/
[Matplotlib]: https://img.shields.io/badge/MATPLOTLIB-V3.6.2-blue?style=for-the-badge&logo=matplotlib
[Matplotlib-url]: https://matplotlib.org/
[Docker]: https://img.shields.io/docker/pulls/mauriciohc/snells-law?logo=docker&style=for-the-badge
[DockerImage-url]: https://hub.docker.com/r/mauriciohc/snells-law

[Docker-url]: https://hub.docker.com/
[Compose-url]: https://github.com/mauriciohc02/Snells-Law_Calculator/blob/main/docker-compose.yml
[Script-url]: https://github.com/mauriciohc02/Snells-Law_Calculator/blob/main/run.sh
