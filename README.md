# Mint Device Screensaver

An animated screensaver inspired by the Linux Mint design language.

The project uses GTK, Clutter, Cairo, and librsvg to render animated SVG device icons over a dynamic particle background. The goal is to create a modern, lightweight screensaver for Linux Mint that is visually appealing while remaining efficient.

## Features

* Animated SVG device icons
* Smooth orbital icon movement
* Depth-based scaling and opacity
* Staggered icon fade-in
* Animated particle background
* Full-screen GTK/Clutter rendering
* Written entirely in Python

## Requirements

Tested on:

* Linux Mint 22.3 (64-bit)

System packages:

* Python 3
* GTK 3
* Clutter
* GtkClutter
* Cairo
* librsvg
* PyGObject (python3-gi)

An installation script (`install-dependencies.sh`) is included to install the required packages on Linux Mint.

## Installation

Clone the repository:

```bash
git clone https://github.com/chaslinux/mint-device-screensaver.git
cd mint-device-screensaver
```

Install dependencies:

```bash
./install-dependencies.sh
```

## Running

From the project root:

```bash
./run.sh
```

Alternatively:

```bash
python3 src/main.py
```

## Project Structure

```
mint-device-screensaver/
├── data/
├── debian/
├── src/
├── install-dependencies.sh
├── run.sh
├── LICENSE
└── README.md
```

## Development

The project is developed using feature branches with incremental commits and Git tags to make experimentation easy while keeping stable milestones.

Typical workflow:

```bash
git checkout -b feature-name
```

After testing:

```bash
git add .
git commit -m "Describe the change"
git tag vX.Y-feature
git push origin feature-name
git push origin vX.Y-feature
```

Stable features are merged into `main`.

## Roadmap

Planned improvements include:

* Native Debian (`.deb`) package
* Cinnamon screensaver integration
* Application launcher
* Desktop entry
* Additional particle effects
* Configuration options
* Improved documentation
* Screenshots and demo video

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

