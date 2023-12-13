# Tetris and Sandtris

This repository includes two games: **Tetris** and **Sandtris**.

 - For the basic rule about Tetris, read the Wikipedia article [here](https://en.wikipedia.org/wiki/Tetris). 
  - Sandtris is basically a Tetris made out of sand -- in order to clear a line, you need to make
   a single color of sand go across the board. You can play a better-developed version [here](https://sandtris.com/).

Implemented by JiWon Woo @Johns Hopkins University.

# How to Use

These two games are built on Python. You can easily download Python by using [Anaconda](https://www.anaconda.com/) environment. 

## Requirements

    more-itertools==10.1.0
    numpy==1.26.1
    scipy==1.11.4
You can download the required packages by running the following code.

    pip install -r requirements.txt

## Running Tetris

You can run Tetris by running  `gameplay.py` in Tetris folder.

## Running Sandtris

You can run Sandtris by running `sandtris_gameplay.py` in Sandtris folder. 


## Commands 

 - Right / Left arrow: Moves the tetromino right and left. 
 - Up Arrow: Rotates the tetromino. 
 - Down Arrow: Increases the falling speed.

# Data Structure

These games are built with object-oriented programming in Python. There are three main classes throughout the repository: **Tetris, Playfield, and Tetromino.**

## Class: Tetris

The Tetris class controls the general gameplay. This includes drawing the falling Tetrominoes, player commands, clearing lines, keeping track of score/level, and checking for game over.

## Class: Playfield

The Playfield class stores fallen, fixed Tetrominoes, and has clear line functionalities. The Playfield class also contains the "Game Over" screen.

## Class: Tetromino

The Tetromino class creates the 7 Tetromino blocks with their appropriate shape and keeps track of the block's orientation. 

## Class: Sandtris

The Sandtris class controls the general gameplay. This includes drawing the falling Tetrominoes, running sand physics, player commands, clearing lines, keeping track of score/level, and checking for game over.

## Class: Sandtris_Playfield

The Sandtris_Playfield class stores fallen fixed Tetrominoes and controls the sand physics. The sand physics includes filling in any gaps and simulating the cascade of sand when individual grains are stacked too high. The Santris_Playfield can also clear "lines" where the same color spreads across the playfield. The Sandtris_Playfield class also contains the "Game Over" screen.

## Class: Sandtromino

The Sandtromino class, like the Tetromino class, is used to create the 7 Tetromino blocks with their appropriate shape and keeps track of the block's orientation. However, the Sandtromino class is scaled so multiple grains of "sand" fit inside a Sandtromino. 
