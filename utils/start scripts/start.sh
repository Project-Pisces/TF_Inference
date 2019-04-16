cd ~/

echo "nvidia" | sudo -S ./jetson_clocks.sh

{ echo "Started GPU MAX Frequency at: "; date; } | tr "\n" " " | tee -a ~/home/nvidia/inference.log && echo

cd /home/nvidia/github/TF_Inference/

sleep 30

sudo python3 /home/nvidia/github/TF_Inference/run_inference.py --graph /home/nvidia/github/TF_Inference/tf_files/mobile_net_fish_of_guadalupe_graph.pb --labels /home/nvidia/github/TF_Inference/tf_files/mobile_net_guadalupe_labels.txt

cd ~/
