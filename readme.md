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

    $ draw-compose -i  -o docker-specific.png
