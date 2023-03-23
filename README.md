[![Python Version](https://img.shields.io/badge/python-%203.9-blue.svg)](https://www.python.org/downloads/)

# Swipe Scorecard
Swipe Scorecard is a web application built with Flask and Python that allows users to keep score of the card game Swipe. The application allows users to add players, add scores for each round, and view the current standings of the game.

## Getting Started
To get started with the Swipe Scorecard application, you'll need to have Python and Flask installed on your computer. You can download Python from the official website at https://www.python.org/downloads/. Once you have Python installed, you can install Flask by running the following command in your terminal:

`pip install Flask==2.1.1 Flask-Session`
Once you have Flask installed, you can run the application by navigating to the root directory of the application in your terminal and running the following command:

`flask run`
This will start the application on your local machine, and you can access it by opening your web browser and navigating to `http://localhost:5000`.

## Usage
To use the Swipe Scorecard application, you can follow these steps:

* **Add players**: Enter the names of the players in the "Players" section of the application and click "Add Player".

* **Add scores**: In the "Add New Round" section of the application, enter the scores for each player in the round and click "Submit Round".

* **View standings**: The current standings of the game will be displayed in the "Current Standings" section of the application.

* **Start a new game**: To start a new game, click the "Start New Game" button in the application.

## Docker

To build and run a Docker container of the application, you can follow these steps:

* **Build the Docker image**: Navigate to the root directory of the application in your terminal and run the following command: `docker build -t swipe-scorecard .` This will build a Docker image of the application.

* **Run the Docker container**: Once the Docker image has been built, you can run the container by running the following command: `docker run -p 5000:5000 swipe-scorecard`

This will start the container and map port `5000` on your local machine to port `5000` in the container. You can access the application by opening your web browser and navigating to `http://localhost:5000`.

## Contributing
If you would like to contribute to the Swipe Scorecard application, you can do so by forking the repository and creating a pull request. We welcome contributions of all kinds, including bug fixes, feature requests, and documentation improvements.

## License
Swipe Scorecard is licensed under the GNU GENERAL PUBLIC LICENSE. See LICENSE for more information.
