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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  

  <h3 align="center">EdvoraAssignment</h3>

  <p align="center">
    Backend apis for my assesmentproject
    <br />
    <br />
    <p View Documentation of this Apis["uportal.in/docs">]</p>
    <p After login and register connect to broadcast["uportal.in/connectBroadcast">]</p>
    ·
    <a href="https://github.com/sakthiRathinam/edvoraassignment/issues">Report Bug</a>
    ·
    <a href="https://github.com/sakthiRathinam/edvoraassignment/issues">Request Feature</a>
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
  </ol>
</details>




### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [FastAPI](https://fastapi.tiangolo.com/)['FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.']
* [Postgres](https://postgresql.org/)['database used for this project]
* [Docker](https://docker.org/)["production ready container always easy switch to any machines"]
* [Github Actions](https://actions.dev/)['added action that will deploy the app to cloud for every new release']
* [Documentation Live Url](http://uportal.in/docs)['uportal.in or ip:8000/docs/']
* [Reverse-Proxy](https://traefik.io/)['used for reverse-proxy if you want to enable https uncommand all the https middleware it will work']
* [UBUNTU AWS SERVER LIVE URL](http://uportal.in/docs)['used ec2 and traefik to make this app live and you can enable the https by just remove the commented lines in docker-compose-traefik and docker-compose.yml files']


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
## How to Use

In the above mention Documentation url click that register and login and go the url uportal.in/connectBroadcast you are now connected to the broadcast and ready to send messages in that ui if you logged out you are session will be gone and again u need to login and navigate to the broadcast to send and receive messages

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* install poetry
  ```sh
  pip install poetry
* install python 3.8
  ```sh
  pyenv install python 3.8

  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

* Running with poetry
* Clone the repo
   ```sh
   git clone https://github.com/sakthiRathinam/edvoraassignment
   ```
* Install python packages
    ```sh
`   poetry install
    ```
* Change the environment variables in settings.py and urls.py in coresingle
     ```sh
`    change environment varialbles to normal variables
``  ```
* open venv
     ```sh
     poetry shell
     ```
* start the server
     ```sh
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
* open venv
     ```sh
     poetry shell
     ```
* start the chat server server
     ```sh
    uvicorn async_app:app --host 0.0.0.0 --port 80 --reload
    ```

* Running with docker
* Clone the repo
   ```sh
   git clone https://github.com/sakthiRathinam/edvoraassignment
   ```
* Install docker and docker-compose
`    
* create local network internal , web , traefik-public
`    Create database and create user or use default user postgres

* change the env key according to you in env folder 

* fire up the containers BY
    ```sh
    docker-compose up
``


   `
   ```



See the [open issues](https://github.com/sakthiRathinam/edvoraassignment) 

<p align="right">(<a href="#top">back to top</a>)</p>




<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@Sakthi Rathinam](sakthiratnam050@gmail.com) 
Project Link: [https://github.com/sakthiRathinam/edvoraassignment](https://github.com/sakthiRathinam/edvoraassignment)

<p align="right">(<a href="#top">back to top</a>)</p>