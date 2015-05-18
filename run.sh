# Kill python and ngrok instances
# sudo pkill python
# sudo pkill ngrok

#run python server
python /home/pi/Desktop/door-bot/main.py >/dev/null 2>&1 &

/usr/local/bin/ngrok http 7770 > /dev/null &

echo 'Waiting for ngrok to run'

## Sleep for 10 seconds, anticipating ngrok's completion
sleep 10

## update our firebase object with the valid ngrok URL

python /home/pi/Desktop/door-bot/get_public_addr.py
echo 'Running on port 7770'
