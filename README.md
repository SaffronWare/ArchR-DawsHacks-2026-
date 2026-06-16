<video width="320" height="240" controls>
  <source src="vid_dem.mp4" type="video/mp4">
</video>
# DawsHacks 2026 Bridge Simulator

A from-scratch 2D bridge physics simulator and automated visual bridge builder built in Python with Pygame for DawsHacks 2026.

This project won **1st place at DawsHacks 2026**.

# Overview

This project simulates bridge structures using a custom physics engine written from scratch. It visualizes nodes, beams, forces, and structural behavior in real time, allowing bridges to be generated, animated, and tested interactively.

The project also includes an automated visual bridge-building system that constructs bridge-like structures procedurally and animates the building process.

# Features

* 2D bridge simulation built from scratch
* Python / Pygame visualization
* Node-and-beam structural model
* Real-time physics updates
* Procedural / automated bridge construction
* Animated bridge-building visualization
* Interactive visual feedback
* Built during DawsHacks 2026

# Motivation

The goal of this project was to combine physics simulation, procedural generation, and visual design into an interactive bridge-building demo. I wanted to build the simulation logic myself rather than relying on a physics engine, so I could better understand how structural constraints and forces can be represented computationally.

# Technical Notes

The bridge is represented as a system of connected points and constraints. Beams act as distance constraints or spring-like connections between nodes, and the simulation updates the structure over time to show how it responds visually.

The automated builder generates bridge structures step by step, making the construction process visible rather than instantly spawning the final bridge.

# Status

This project was built as a hackathon prototype, so the code prioritizes rapid experimentation and visual demonstration over long-term architecture.

Future improvements could include:

* More realistic force calculations
* Stress visualization
* Better failure/breaking mechanics
* Improved procedural bridge optimization
* User-editable bridge designs
* Cleaner UI and controls

# Running the Project

Install Python and Pygame, then run the main file:

```bash
pip install pygame
python main.py
```

The exact entry file may vary depending on the current repository structure.
