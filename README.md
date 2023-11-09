# Maintainability Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/cd1e970a06b36675ebe4/maintainability)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-TomasSchugurensky/maintainability)

# Test Coverage Badge
[![Test Coverage](https://api.codeclimate.com/v1/badges/cd1e970a06b36675ebe4/test_coverage)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-TomasSchugurensky/test_coverage)

# CircleCI main badge
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-TomasSchugurensky/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-TomasSchugurensky/tree/main)

# Game
This code try to simulate the board game "Scrabble" via text messages directly in terminal

# Rules
Start: Each player takes 7 tiles at random from the set of tiles, you can exchange it if you want but it skips a turn

Gameplay: Players must form words on the board using their tiles. The words must be put in valid coordinates on a board which has 15x15 cells. Those words should be validated by a dictcionary (in this case the spanish dictionary also know as RAE)

You can also skip turns and end the game if you want

# How to run it on Docker
1. Have Docker installed, here's the website (https://www.docker.com/get-started) if you don't know how to do it

2. Install Git via Terminal: $apt-get install git

3. Clone the repository: $git@github.com:um-computacion-tm/scrabble-2023-TomasSchugurensky.git

4. Navigate to the repository using cd

5. Build the Docker image: $docker build -t "image_name"  (In image name give it the name you want without the brackets)

6. Run the Docker image: $docker run "image_name"