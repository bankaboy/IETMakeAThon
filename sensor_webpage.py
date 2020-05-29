from flask import Flask, render_template, request, flash, request, redirect, url_for,jsonify
import serial
from random import randint
from time import time
import threading
import os
import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np
from graph_maker import create_graph

app = Flask(__name__)
std_values = [6.5,25.00,87]

ser = serial.Serial('/dev/ttyACM1',9600) #connect to arduino

global ph,temp,moisture,readings

def getValues(ser):
    global readings,ph,temp,moisture
    while True:
        readings = ser.readline()
        #readings = os.sys('cat /dev/ACM0')
        reading = readings.decode('ascii')
        #print(reading)
        reading = reading.strip()
        results = reading.split(',')
        #create_graph(std_values,results)
        print(results)
        create_graph(std_values,results)
        ph =    results[0]
        temp = results[1]
        moisture = results[2]


t = threading.Thread(target = getValues,args=(ser,))
t.start()

page = 'This is the page to display sensor values'

@app.route("/")
def renderHome():
        return render_template("index.html")

@app.route("/getSensor")
def returnSensor():
        global ser,ph,temp,moisture
#     if request.method == "GET":
        #values = {}
       # values['temperatureValue'] = randint(20, 50)
        #values['phValue'] = randint(3, 8)
        #values['moistureValue'] = randint(40, 80)
        #values['humidityValue'] = randint(50, 100)
        #return jsonify(values = values)
        #readings = ser.read()  # read sensor values from serial
        #result = str(readings).split(',')  # split into 3 and then assign to appropriate variable
        #readings = str(ser.readline())
        #readings = readings.strip()
        #result = readings.split(',')
        #print(readings)
        #ph = result[0]
        #temp = result[1]
        #moisture = result[2]
        #time.sleep(1)
        #temp = result[1]
        #moisture = result[2]
        #temp = randint(20,50)
        #moisture = randint(40,80)
        #print("VAlue: ", ph)
        # return render_template("index.html", ph=ph,temp = temp, moisture = moisture)
       #temp=temp, ph=ph , moisture=moisture
        return jsonify(ph=ph,temp=temp,moisture=moisture)

if __name__ == '__main__':
    app.run(debug = True,port='3000')


