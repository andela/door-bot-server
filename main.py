import RPi.GPIO as GPIO
import time
from flask import Flask
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

@app.route("/open/")
def openDoor():
        GPIO.output(18, 1)
	time.sleep(1)
	GPIO.output(18, 0)
    	status = "Main Door is opened"
    	return status



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7770)
GPIO.cleanup()
