# PyData Amsterdam 2023 workshop materials

## For workshop participants

You have three options for running the software for this workshop. They are listed from easiest to hardest:

### Quick Start (using colab)

You can open the exercises in Google's Colab with the button below:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/datakami/pydata-llama-index-tutorial/blob/main/Colab-Exercises.ipynb)

### Quick Start (using docker)

This assumes you have Docker and git installed. The image takes about 1.7GB of disk space.

```
$ git clone https://github.com/datakami/pydata-llama-index-tutorial.git
$ cd ./pydata-llama-index-tutorial
$ docker run -it --rm -v $PWD:/repo -p 127.0.0.1:8888:8888 ghcr.io/datakami/llamaindex-workshop:latest
```
In the output, find the line saying "Jupyter Server 2.7.3 is running at:", and click the link starting with `http://127.0.0.1:8888`. Jupyterlab should launch in your browser. Open the `Exercises-1.ipynb` file to get started.

### Quick Start (no docker)

This assumes you have git and Python 3.8 - 3.11 installed.
```
$ git clone https://github.com/datakami/pydata-llama-index-tutorial.git
$ cd ./pydata-llama-index-tutorial
$ python -m venv ./venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python check_installation.py
$ jupyter-notebook
```

Jupyterlab should launch in your browser. Open the `Exercises-1.ipynb` file to get started.

## Explanation: Repository structure

There are a few different files:

- `Exercises-*.ipynb`: These files contain exercises for workshop participants. Participants are meant to use these.
- `Colab-*.ipynb`: merged notebooks that can be used to run this workshop in colab.
- `Solutions-*.ipynb`: also contain answers. Used to generate the exercises notebooks.
- `check_installation.py`: can be used to check that all dependencies are set up correctly and download the necessary models.
- `data/`, `indices/`: workshop data and vector indices, used in the exercises.
- `Build-*.ipynb`: notebooks to prepare the workshop data and vector indices.
- `build/`: code to generate the exercises and colab notebooks.

## For contributors
### When committing

```
$ nb-clean clean -o [yournotebook.ipynb]
```

### Building Exercises from Solutions
Solution filenames should start with "Solutions-". Code cells that start with a "#" are converted to questions with empty answers.
```
$ python -m build
```
