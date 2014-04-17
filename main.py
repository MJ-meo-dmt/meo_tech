#!/usr/bin/python

################
# The MIT License (MIT)
#
# Copyright (c) <2013> <Martin de Bruyn>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
############################################################

#----------------------------------------------------------------------#

"""@ package MeoTech

Handle the setup of the whole app.
"""

# System Imports
import sys
import os
import logging as log

# Panda Engine Imports
from pandac.PandaModules import loadPrcFileData
loadPrcFileData("",
"""
    window-title OWP - QuickShadows
    fullscreen 0
    win-size 1200 600
    cursor-hidden 0
    show-frame-rate-meter 1
    #want-tk 1
    #want-directtools 1
"""
)

from direct.showbase.ShowBase import ShowBase

# MeoTech Imports
from engine.engine import Engine
from game.game import Game

#----------------------------------------------------------------------#

# Notes on [rising]
"""
"Soft Re-write on rising, depending on all the features... then build it into the meotech engine while furthering developing on the MeoTech
engine itself.  Then on release we give the player the game and the "engine" (with simpler tools) so that they can mod the game.  :-) They may learn some stuff about

So the idea would be to, take all the gameplay stuff from rising or something similar and then create the game using the meotech stuff and the way it connects to 
blender... or we have to swap it around and take some of the meotech stuff and infuse that witht he current rising code... either way.. i think though that getting the
game play and game mechanics sorted first would be simler and faster than trying to convert everything in the old code to use the blender style way or it could be easy
lol i dono.. either way will be work so im up with whatever... id like to finish something...

I think we should start making tools that we can use to create the game itself.

oh and what about checking out 2 camera modes.. 3rd and 1st...

"""


# Main App
class MeoTech(ShowBase):
    """MeoTech Main Class.
    
    Handles the setup of the whole app.
    Basically connects the MeoTech Engine with the Game Engine.
    """
    
    def __init__(self):
        
        # Create the main app Log file
        log.basicConfig(
                        filename="MeoTech.log",
                        level=log.DEBUG,
                        format="%(asctime)s %(levelname)s: %(message)s",
                        datafmt="%d-%m-%Y %H:%M:%S")
        
        
        # Init Panda
        ShowBase.__init__(self)
        
        # Init Engine
        self.engine = Engine(self)
        
        # Init Game
        self.game = Game(self)
        
        # Debug stuff
        wantDebug = True
        
        if wantDebug:
            self.engine.showBulletDebug()
            print " "
            print "Panda Render.ls()"
            print "--------------------------------------------------------"
            print render.ls()
            print "--------------------------------------------------------"


meotech = MeoTech()
run()
































