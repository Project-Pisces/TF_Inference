# TF_Inference
This repository contains the code needed to run inference on the Tensorflow generated frozen graph (model) along with the needed resources to build it again.

To run properly both `snapshot.py` and `run_inference.py` must be running at the same time and throught the duration of the exploration. 

1. **`snapshots.py`** process uses openCV to capture an image from the main web cam at 12fps by default
2. **`run_inference.py`** ensures that the directory being used is not empty, if it is then there is a buffer of time on which the snapshot process is allowed to catch-up
3. Once the image has been read and inference run we store or or ignore the image based on the results we found.
4. Images are removed from directory to prevent wasted space

![img](assets/proc.JPG)

This is the current tree structure of the project note that `run_inference.py` must be on the parent directory of 

`/tf_files/mobile_net_fish_of_guadalupe_graph.pb` 

and 

`/tf_files/mobile_net_guadalupe_labels.txt`

~~~bash
/
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
