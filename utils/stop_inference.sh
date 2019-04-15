if [kill $(ps aux | grep '[p]ython snapshots.py' | awk '{print $2}')]
then
  echo "Killed Snapshots application"
fi

if [kill $(ps aux | grep '[p]ython run_inference.py' | awk '{print $2}')]
then
  echo "Killed inference application"
fi


