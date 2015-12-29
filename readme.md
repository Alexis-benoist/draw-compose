# Draw compose

Render compose files with one command line!

This project needs graphviz installed.

## Simple example

![Simple example](https://raw.githubusercontent.com/Alexis-benoist/draw-compose/master/fixtures/simple.png?raw=true "Simple Example")

## Classic python example
![Python classic](https://raw.githubusercontent.com/Alexis-benoist/draw-compose/master/fixtures/real.png?raw=true "Python web app")

# Install
## On OSX:
Install graphviz `brew install graphviz` and draw-compose:

    $ pip install draw-compose

# Use

Renders by default `docker-compose.yml` in the current folder.

    $ draw-compose -o docker.png

Or a specific docker file can be rendered:

    $ draw-compose -i fixtures/real.yml -o docker-specific.png

# Notes
Released under an Apache License 2.0

Similar: [docker-compose-graphviz](https://github.com/abesto/docker-compose-graphviz) written in GoLang

Creator: Alexis Benoist @Alexis_Benoist

Inspired by [ERAlchemy](https://github.com/Alexis-benoist/ERAlchemy)
