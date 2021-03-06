<p align="center">
  <a href="https://github.com/1bayezian/nevo">
    <img src="/images/logo.png" alt="evo" width="125" />
  </a>
</p>
<h3 align="center">evo</h3>
<p align="center">
  A neuroevolution framework for training agents on OpenAI Gym.
</p>

## Table of Contents

- [Key Features](#key-features)
- [Download](#download)
- [Usage](#usage)

## Key Features

* A simple command line interface (CLI) to train and test game AI developed with neuroevolution on Open AI gym.
* Cross platform
  - Windows, macOS and Linux ready.

## Download

To clone and run this application, you'll need [Git](https://git-scm.com) and [python3](https://www.python.org/download/releases/3.0/) (which comes with [pip3](https://pypi.org/project/pip/)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/1bayezian/evo

# Go into the repository
$ cd evo

# Install CLI tool and dependencies
$ pip3 install .

# Run the help command
$ evo --help
```

## Usage

##### Sample Usage
```
  evo --mode=TRAIN --epochs=10000 --env=CartPole-v0 --new=TRUE 
  evo --mode=TEST --epochs=10 --model=~/Users/models/trained.model
```