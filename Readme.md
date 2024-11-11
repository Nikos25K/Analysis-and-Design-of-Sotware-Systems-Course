# Analysis and Design of Sotware Systems Course Project

## Repository Overview

This repository contains the project work for the Analysis and Design of Sotware Systems course at Department of Informatics & Telecommunications - NKUA. <br>


## Assignment 1: Game Application UML Diagrams and Structured Analysis

This repository contains the complete UML diagrams and structured analysis for a game application developed as part of a university assignment. The project models a game system where users can participate either as spectators or players. Players form teams, interact in a 3D world, and manage team roles while navigating challenges influenced by entropy and energy mechanics. The objective is to provide a detailed architectural and behavioral model of the application, covering both user interactions and the game’s mechanics.

The project is divided into two main parts:

### Application (Part A)
This part addresses the account setup, login/logout mechanisms, and spectator functionalities.

### Game Mechanics (Part B)
This part covers in-game interactions and the roles of digital team members, including rules for energy, entropy, and game-winning conditions.

## Project Objectives

This assignment aims to develop students' understanding of UML modeling and system design. Through this project, students will:

- Model a complex system using various UML diagrams to represent structure and behavior.
- Explore class relationships and dependencies, focusing on visibility, associations, and methods.
- Design a system with game mechanics, covering elements like entropy management, energy levels, and player interactions in a 3D world.
- Develop structured analysis skills, producing a Data Flow Diagram (DFD) to summarize and represent system functions.

## Diagrams and Their Descriptions

### Use Case Diagram
Depicts the high-level interactions between actors (such as spectators and players) and the system, highlighting all possible user actions and relationships like inclusion, extension, and generalization where appropriate.

### Class Diagram
Shows the structure of the system by detailing classes, attributes, methods, and relationships among classes. It captures visibility (private, public, protected), data types (e.g., Integer, Boolean), and parameters for methods, modeling the application's core and game components.

### Sequence Diagrams
Represents interaction sequences for specific scenarios, such as activating the Defender for defense, using the Collector to gather items, or triggering the Medic for healing. Each diagram illustrates the flow of messages between objects in a particular scenario.

### Statechart Diagrams
Models the lifecycle of specific entities like the game world and a player’s team, representing states and transitions triggered by events (e.g., switching between day/night or when entropy changes).

### Activity Diagrams
Demonstrates workflows for key actions (e.g., activating the Medic, Defender, Explorer, and Collector) and the general gameplay flow. Each diagram represents decision points, loops, and sub-activities to capture complex behavior.

### Data Flow Diagram (DFD)
Provides an abstract view (Level 1) of data processing in the application, mapping out inputs, outputs, and data stores involved in user interactions and game state management.


## Bonus

This project is an extension of a previously designed system developed for the Software Design course, focused on further expanding its functionality through additional object-oriented analysis and design. This expansion is based on specific requirements gathered through a user interview and includes the addition of new classes and features to enhance the system’s capabilities.

## Key Steps

### Requirements Gathering
The project began with a structured interview with the user to gather requirements for the system's expansion. Together, we documented and anonymized the interview insights, which then guided our approach to the object-oriented analysis and design.

### Object-Oriented Analysis & Design
Building on the initial design, we introduced new classes to meet the updated requirements:

- As a collaborative project, we developed more than four new classes to extend the system’s functionality, carefully aligning with principles like encapsulation and modularity to ensure cohesive integration.
- We created class diagrams to illustrate the relationships and attributes of each new class, available in the 02_Design folder. Additionally, we included a secondary diagram depicting another core aspect of the expanded system.

### Implementation
Using Python, we implemented the new classes with complete attributes and methods, ensuring that each class fulfills its intended role within the system. The code is structured to work seamlessly with the initial implementation, with a focus on maintainability and scalability.

### Testing and Continuous Integration
We developed unit tests to validate each new class, with at least two tests per class to verify functionality and robustness. These tests were integrated with GitHub Actions, allowing continuous monitoring of code integrity. All tests passed successfully, confirming the reliability of the expanded functionality.

### Repository Structure
The project repository adheres to course guidelines and is organized into designated folders:

- **01_Requirements**: Contains the anonymized transcript of the user interview.
- **02_Design**: Includes class diagrams and additional system diagrams in PDF format.
- **03_Code**: Contains the source code of the new classes and the unit tests we developed to verify them.