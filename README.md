# TF_Inference

This repository contains the code needed to run inference on the Tensorflow generated frozen graph (model) along with the needed resources to build it again.

- [Overview and dependencies](#overview-and-dependencies)
- [Project Architecture](#project-architecture)
- [How to run inference](#how-to-run-inference)
- [Results explained](#what-is-happening)
- [Future improvements](#future-improvements)

## Overview and dependencies

To run properly both `snapshot.py` and `run_inference.py` must be running at the same time and through the duration of the exploration.

1. **`snapshots.py`** process uses openCV to capture an image from the main web cam at 12fps by default
2. **`run_inference.py`** ensures that the directory being used is not empty, if it is then there is a buffer of time on which the snapshot process is allowed to catch-up
3. Once the image has been read and inference run we store or or ignore the image based on the results we found.
4. Images are removed from directory to prevent wasted space

## Project architecture

![img](assets/proc.jpg)

This is the current tree structure of the project note that `run_inference.py` must be on the parent directory of:
`/tf_files/mobile_net_fish_of_guadalupe_graph.pb` and `/tf_files/mobile_net_guadalupe_labels.txt`

~~~bash
TF_inference
|
├── README.md
├── assets
├── run_inference.py
├── snapshots.py
└── tf_files
    ├── bottlenecks
    ├── mobile_net_fish_of_guadalupe_graph.pb
    ├── mobile_net_guadalupe_labels.txt
    ├── models
    └── training_summaries
~~~

## How to run inference

In order to execute the program ensure you have these Python packages installed and have sourced your virtual environment if you're using one

~~~bash
Keras-Applications==1.0.7
opencv-python==4.0.0.21
protobuf==3.7.0
tensorflow==1.13.1
tensorflow-hub==0.3.0
~~~

Finally run both processes to get started

~~~bash
python snapshots.py
~~~

~~~bash
python3 run_inference.py \
--graph tf_files/mobile_net_fish_of_guadalupe_graph.pb \
--labels tf_files/mobile_net_guadalupe_labels.txt
~~~

you know you did it right if this is your output:

![img](assets/OMG-chinook-tztnic-768x505.png)

Note that we have disabled the email function for now, it is functional but we do not have reliable wireless connectivity as of now

### What is happening

As you see from the architecture diagram, inference is constantly run and when an image is of interest it is stored on disk. Take a look at the image below, it is a paper printout of a chinook salmon which was identified and stored on a new directory:

![img](assets/Internet-Chinook-su2a4m-768x514.png)

## Future improvements

New data on the target fish is desperately needed