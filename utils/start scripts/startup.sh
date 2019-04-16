
sleep 10

echo "nvidia" | sudo -S ./jetson_clocks.sh

echo "Started GPU MAX Frequency" | tee -a ~/Desktop/inference.log

sleep 5

cd /home/nvidia/github/TF_Inference/
python snapshots.py --usb_cam=True &

cd ~ 
