"""
    File: app_design.py
    Abstract: This class will pull together all the necessary functions to make the main
                program run correctly.
    Date: 12/15/2020
    Author: Brendon Magana for CST 205

"""

#these are our classes that we worked on 
from passwordG import MainApp

import main


#imports that are needed to make the program run

# https://kivy.org/doc/stable/api-index.htmls
import os
import kivy
from kivy.config import Config

kivy.require("1.9.1") 

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from colour import Color
from kivy.core.clipboard import Clipboard
from kivy.core import window
# from core import logger
import pyperclip
import random

#app = MainApp()


if __name__ == '__main__':

    # location = googlemap()
    # print(location)
    # stringp = main()

    ps = main
    stringp = ps.ps()
    
    #print(stringp)

    app = MainApp()
    app.setPS(stringp)
    app.run()
    