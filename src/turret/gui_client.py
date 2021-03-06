#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from tkinter import *
import time
import math
import sys
from turret_command import TurretCommand as command

servo = command.ServoState
laser = command.LaserState

laserstate = True

HOST, PORT = "129.16.197.34", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

master = Tk()

canvas_width = 800
canvas_height = 600
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

keys = dict()
coords = []
data = command()
i = 0
x = 140
y = 140

def timer_function():
    handle_tcp()
    test_function()
    w.create_text((canvas_width/2,20),text=str(keys))
    master.after(20, timer_function)

def handle_tcp():
    global laserstate
    #data = command()
    global data
    #if laserstate:
    #    data.laser = laser.on
    #else:
    #    data.laser = laser.off
    if 113 in keys and keys[113]:
        data.servo_x = servo.inc
    if 114 in keys and keys[114]:
        data.servo_x = servo.dec
    if 111 in keys and keys[111]:
        data.servo_y = servo.inc
    if 116 in keys and keys[116]:
        data.servo_y = servo.dec
    data.laser = laser.off
    print(data.laser)
    if False:
        laserstate = laser.off
        #if laserstate:
        #    data.laser = laser.on
        #else:
        #    data.laser = laser.off
    if (not data.servo_x == 0 and not data.servo_y == 0):
        sock.send(bytes(data))
        status = sock.recv(1)
        try:
            if not int.from_bytes(status, 'little'):
                sys.exit()
        except:
            pass

def test_function():
    global coords, i, x, y, data
    i += 1
    #print(data.servo_x)
    if data.servo_x == 2:
        x += 5
    if data.servo_x == 1:
        x -= 5
    if data.servo_y == 2:
        y += 5
    if data.servo_y == 1:
        y -= 5
    #print(data.servo_y)
    #print(data.laser)
    #x = int(100*math.sin(math.radians(i)*4 )) 
    #y = int(100*math.cos(math.radians(i)*4 ))

    coords.append((x,y))

    w.delete('all')
    '''
    for a,b in zip([i for i in coords ],[i for i in coords[1:]]):
        w.create_line(a[0]*2+(canvas_width/2), a[1]*2+(canvas_height/2),
                b[0]*2+(canvas_width/2), b[1]*2+(canvas_height/2),
                fill="#476042", width=4)
    '''
    for a,b in zip([i for i in coords ],[i for i in coords[1:]]):
        w.create_line(a[0],a[1],b[0],b[1],fill="#476042", width=4)

    if len(coords) > 10:
        coords.pop(0)
    data = command()

def KeyPressed(event):
    keys[event.keycode] = 1
    #print(event.keycode)
def KeyReleased(event):
    keys[event.keycode] = 0
    #print(event.keycode)

master.after(200, timer_function )
master.bind_all('<KeyPress-Up>', KeyPressed)
master.bind_all('<KeyRelease-Up>', KeyReleased)
master.bind_all('<KeyPress-Down>', KeyPressed)
master.bind_all('<KeyRelease-Down>', KeyReleased)
master.bind_all('<KeyPress-Left>', KeyPressed)
master.bind_all('<KeyRelease-Left>', KeyReleased)
master.bind_all('<KeyPress-Right>', KeyPressed)
master.bind_all('<KeyRelease-Right>', KeyReleased)
master.bind_all('<KeyPress-space>', KeyPressed)
master.bind_all('<KeyRelease-space>', KeyReleased)
try:
    sock.connect((HOST, PORT))
    mainloop()
finally:
    sock.close()
