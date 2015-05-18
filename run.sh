# Kill python and ngrok instances
sudo pkill python
sudo pkill ngrok

#run python server
sudo python main.py >/dev/null 2>&1 &

ngrok http 7770 >/dev/null 2>&1 &

echo 'Waiting for ngrok to run'

## Sleep for 5 seconds, anticipating ngrok's completion
sleep 5

## update our firebase object with the valid ngrok URL
python get_public_addr.py
echo 'Running on port 7770'