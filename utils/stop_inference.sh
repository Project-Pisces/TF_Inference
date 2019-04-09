if kill $(ps aux | grep '[p]ython snapshots.py' | awk '{print $2}'); then
  echo "Killed Snapshots application"
else
  echo "Failed to stop Snapshots application. Is it running?"
fi

if kill $(ps aux | grep '[p]ython run_inference.py' | awk '{print $2}'); then
  echo "Killed inference application"
else
  echo "Failed to stop Snapshots application. Is it running?"
fi


