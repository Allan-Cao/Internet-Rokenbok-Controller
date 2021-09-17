# Based on the work of simonvc https://github.com/simonvc/rover-wasd-server

import serial
import serial.tools.list_ports
import time
import cv2
from flask import Flask, render_template, request, Response
from importlib import import_module
import os
Camera = import_module('camera_opencv').Camera

camera = cv2.VideoCapture(0)

ser = serial.Serial("/dev/ttyACM0",baudrate=250000)

app = Flask(__name__)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/")
def hello():
  return "You probably want <a href=/static/rover.html> to control the rover. </a>"

# Select
@app.route("/select")
def select():
	print("select")
	ser.write(b"0")
	#time.sleep(0.1)
	return("select")

# STOP command
@app.route("/stop")
def stop():
	print("stop")
	ser.write(b"1")
	return("stop")
@app.route("/down")
def down():
	print("down")
	ser.write(b"4")
	return("down")
@app.route("/up")
def up():
	print("up")
	ser.write(b"6")
	return("up")
# WASD

@app.route("/w")
def w():
	print("w")
	ser.write(b"w")
	#time.sleep(0.1)
	return("w")
@app.route("/a")
def a():
	print("a")
	ser.write(b"a")
	#time.sleep(0.1)
	return("a")
@app.route("/s")
def s():
	print("s")
	ser.write(b"s")
	#time.sleep(0.1)
	return("s")
@app.route("/d")
def d():
	print("d")
	ser.write(b"d")
	#time.sleep(0.1)
	return("d")
# Q E
@app.route("/q")
def q():
	print("q")
	ser.write(b"q")
	#time.sleep(0.1)
	return("q")
@app.route("/e")
def e():
	print("e")
	ser.write(b"e")
	#time.sleep(0.1)
	return("e")
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True, use_reloader=False, threaded=True)

