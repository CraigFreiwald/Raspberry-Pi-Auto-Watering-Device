# Auto-Watering Program
# by: Craig Freiwald
# for: IST-402
# created: 4/1/2022
# last edited: 4/29/2022

#------------Imports-----------------
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import time
import RPi.GPIO as GPIO

#this setting is necesarry or program will print non-important error while still functioning
GPIO.setwarnings(False) 

#------------GPIO setup-----------------
#BCM mode for ease of GPIO mapping
GPIO.setmode(GPIO.BCM)
#BCM pin 21 as moisture sensor input
GPIO.setup(21,GPIO.IN)
#BCM pin 26 as output signal to relay
GPIO.setup(26,GPIO.OUT)


#------------Watering Function----------
def turnOn():
    
    endTime = time.time() + (3600 * (float(num1.get())))
    
    messagebox.showinfo(title="Auto-Gardener", message='Click Ok to Activate Auto-Watering')
    
    while time.time() < endTime:
            
        if (GPIO.input(21))==0:
            print('Wet')
            GPIO.output(26, GPIO.HIGH)
                
        elif (GPIO.input(21))==1:
            print('Dry')
            GPIO.output(26, GPIO.LOW)
            print('Pump  on')
                
                 
        time.sleep(.5)
    GPIO.output(26, GPIO.HIGH)
    

#------------GUI Set-up-----------------

root = tk.Tk()
root.title("Auto-Watering Device")
root.geometry("220x310")
path = "roboGarden.jpeg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img).grid(row=0, column=0, columnspan = 3)
num1 = tk.StringVar()
tk.Label(root, text="Amount of Hours:").grid(row=1, column=1)
tk.Entry(root, textvariable=num1).grid(row=2, column=1)
button = tk.Button(root, text="Turn on Auto-Watering", command=turnOn)
button.grid(row=3, column=1)


#------------Main Run-----------------
root.mainloop()