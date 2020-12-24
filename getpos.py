#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pynput
import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

alongtime = 999

def getPosition():
    print ("Current position: " + str(mouse.position))
    time.sleep(alongtime)
getPosition()