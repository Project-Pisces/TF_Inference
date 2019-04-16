#!/bin/bash

echo "PID of snapshots.py: "
ps aux | grep '[p]ython snapshots.py' | awk '{print $2}'

echo "PID of run_inference.py: "
ps aux | grep '[p]ython run_inference.py' | awk '{print $2}'
