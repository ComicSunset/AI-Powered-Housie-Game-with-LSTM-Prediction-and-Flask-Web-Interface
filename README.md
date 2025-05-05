## 🎲 AI-Powered Housie Game 🧠 with LSTM Prediction and Flask Web Interface 🌐

# 📜 Overview

This project brings the classic Housie (or Bingo) game into the digital age by combining AI and web technology. It is an AI-powered Housie game that uses LSTM (Long Short-Term Memory) for number prediction. The game is hosted on a Flask web interface, providing an interactive and seamless user experience.

The game features:

Automated gameplay with random number calling.

LSTM-based prediction for forecasting the next number to be called.

Winner detection when a player completes a row, middle line, last line, or full card.

Interactive web interface for easy interaction with the game.

# 🚀 Features

Automated Gameplay: The game automatically calls numbers and updates player cards.

LSTM Number Prediction: The next number is predicted based on historical data using a trained LSTM model.

Flask Web Interface: A user-friendly interface built with Flask to control and view the game.

Winner Detection: The game identifies the winner based on the completion of lines on a player's card.

Multi-Player Mode: Two computer players compete against each other in the game.

# 🛠️ Technologies Used

Python 3.x: The programming language used for game logic and backend development.

Flask: A lightweight Python web framework to build the web interface and handle game actions.

TensorFlow/Keras: Libraries used to create and train the LSTM model for number prediction.

HTML/CSS/JavaScript: Frontend technologies for rendering and interacting with the game in a web browser.

NumPy/Pandas: Used for data manipulation and processing.

# 🎮 How to Play

Game Start: Once you open the web page, the game will start automatically, with numbers being called in real time.

Number Calling: Random numbers are called, and both players’ cards are updated accordingly.

LSTM Prediction: At each step, the model predicts the next number based on the historical sequence of called numbers.

Winner Detection: The game checks if either player completes a row, middle line, last line, or full card and declares a winner.

Game End: The game will announce the winner and stop once a player wins.

# 📈 LSTM Model

The LSTM (Long Short-Term Memory) model is trained to predict the next number based on the sequence of numbers that have already been called. It uses the following approach:

Training: The model is trained using sequences of numbers, and the next number in the sequence is predicted.

Prediction: During gameplay, the model predicts the next number in the sequence based on the current data.

Evaluation: After the model is trained, it is used during the game to generate predictions for the next number.

Model Architecture

The LSTM model uses the following layers:

LSTM Layer: To capture temporal patterns in the sequence of called numbers.

Dense Layer: For final prediction of the next number in the sequence.

The model is trained with random sequences of numbers and is capable of predicting future numbers based on the learned data.

# 🔧 Requirements
To run this project, you need the following Python libraries:

Flask: To build the web interface.

TensorFlow: For building and training the LSTM model.

Keras: High-level API for TensorFlow to work with neural networks.

NumPy: For numerical computations.

Pandas: For handling data.

# screenshot of the gaming interface

![Screenshot (27)](https://github.com/user-attachments/assets/3ffa5476-9b91-4cba-956e-765eec02ffaa)






