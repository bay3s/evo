<p align="center">
  <a href="https://github.com/1bayezian/nevo">
    <img src="/images/logo.png" alt="nevo" width="125" />
  </a>
</p>
<h3 align="center">nevo</h3>
<p align="center">
  A neuroevolution framework for training agents on OpenAI Gym.
</p>

## Table of Contents

- [Key Features](#key-features)
- [Download](#download)
- [Usage](#usage)

## Key Features

* A simple command line interface (CLI) to develop Game AI with neuroevolution.
* Cross platform
  - Windows, macOS and Linux ready.

## Download

To clone and run this application, you'll need [Git](https://git-scm.com) and [python3](https://www.python.org/download/releases/3.0/) (which comes with [pip3](https://pypi.org/project/pip/)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/1bayezian/nevo

# Go into the repository
$ cd nevo

# Install CLI tool and dependencies
$ pip3 install .

# Run the help command
$ nevo --help
```

## Usage

##### Sample Usage
```
  NEVO --mode=TRAIN --epochs=10000 --env=CartPole-v0 --new=TRUE 
  NEVO --mode=TEST --epochs=10 --model=~/Users/models/trained.model
```