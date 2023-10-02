# OOP Adventure Game GUI

![Game Screenshot](imagesGUI/Adventure_Game_Screenshot.png)

## Overview

"OOP Adventure Game GUI" is an interactive graphical user interface (GUI) version of the classic text-based adventure game. The project leverages Object-Oriented Programming (OOP) principles and utilizes the Tkinter library for GUI development in Python.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Deliverables](#deliverables)
- [Application Domain](#application-domain)
- [Getting Started](#getting-started)
- [Instructions](#instructions)
- [Objective](#objective)
- [Class Descriptions](#class-descriptions)
- [Methods and Functionality](#methods-and-functionality)
- [Log of Player's Journey](#log-of-players-journey)
- [Error Prevention and Recovery](#error-prevention-and-recovery)
- [References](#references)

## Description

This project transforms a text-based adventure game into a visually appealing GUI-based game. It incorporates visual images, navigation buttons, and interactive elements to enhance the gaming experience. The implementation follows OOP principles, ensuring high cohesion and low coupling.

## Requirements

- OOP-based Python program
- GUI development using Tkinter
- Visual representation of rooms and items
- Incorporation of tutor-suggested improvements
- Log of the user's journey
- Exception handlers for error prevention and recovery
- Class and method-level documentation

## Deliverables

- Problem statement
- UML class diagram
- Description of the modification from the Assignment 1 program

## Application Domain

The application domain for this project is Game Development. The analysis involves identifying the problem statement, gathering knowledge about class interactions, and implementing images within different frames of the main window.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/mpurvesh007/OOPAdventureGAMEGUI.git
    ```

2. Run the `AdventureWorldGUI.py` file using IDLE or another suitable Python environment.

## Instructions

1. After running `AdventureWorldGUI.py`, a window will prompt you to enter the player's name.
2. The main gameplay window will appear with command buttons and interactive elements.
3. Command words are in the form of a tuple, e.g., typing "go east" and pressing the "run command" button will move you in the east direction.
4. Use navigation buttons, the "run command" button, and interactive item images to explore and play the game.

## Objective

Achieve victory by collecting two specific items in the player's backpack ("money" and "diamonds") after visiting all rooms.

## Class Descriptions

### GUI Class

- Maintains high cohesion and low coupling.
- Contains methods to display and run the game.
- Two frames for displaying text/images and user input.
- Acts as both the view and controller.

### Game Class

- Represents the model, defining data structures and game assets.
- Maintains low coupling with the GUI class.
- Couples the user interface to the GUI.

### Room Class

- Describes room assets, exits, and item functionalities.
- Dependent on Player and Game Class.

### Player Class

- Simple class with an initializing method for the player's name.

## Methods and Functionality

For detailed information about class methods and their functionality, refer to the [Methods and Functionality](#methods-and-functionality) section in this README.

## Log of Player's Journey

A logging library is used to create and update the player's movements inside different rooms. The log is stored in a file named `Player_Journey.log`.

## Error Prevention and Recovery

The init method of the App class utilizes try and except for error prevention.

## References

- [Computer Science Topics](https://www.sciencedirect.com › topics › computer-science)
- [DSM Forum - Domain-Specific Modeling](http://www.dsmforum.org/events/dsm06/Papers/1-Furtado.pdf)
- [Difference between Grid and Pack Geometry Managers in Tkinter](https://www.tutorialspoint.com/difference-between-grid-and-pack-geometry-managers-in-tkinter)

Feel free to explore and enjoy the game!

