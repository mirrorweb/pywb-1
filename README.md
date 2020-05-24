# PyWB2 Warcserver

## Overview

This is a stripped down branch of PyWB2 intended to just provide the functionality to build the bundled
warcserver to run as a standalone application.

Some minimal work has been done to strip out some files for the sake of confusion but otherwise not too
much work on the original code has been done.

## Usage

The warcsever can be build and run via docker, commands are available via the Makefile.

- `make env`
Build the local environment
- `make build`
Build a docker container from the local environment. The deafault TAG (dev) can be overidden with TAG=
- `make run`
Runs the built docker container and exposes the warcserver on port 5005

 