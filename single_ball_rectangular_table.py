#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @file: single_ball_rectangular_table.py
# @author: Lucas Martins 20065236
# @brief: A single ball bouncing around inside a rectangular table
# @project: python pool table a
from __future__ import print_function, division
from visual import *

# constants
radius = 1 # ball radius and standard unit length for simulation
width, height = 40*radius, 60*radius

table = box(pos=(0,0,-radius-0.1), size=(width,height,0.2), color=(0.2,0.5,.1))
wallRight = box(pos=(width/2,0,-radius-0.1), size=(radius,height+radius,2*radius), color=(.4,.2,0))
wallLeft = box(pos=(-width/2,0,-radius-0.1), size=(radius,height+radius,2*radius), color=(.4,.2,0))
wallTop = box(pos=(0,height/2,-radius-0.1), size=(width+radius,radius,2*radius), color=(.4,.2,0))
wallBottom = box(pos=(0,-height/2,-radius-0.1), size=(width+radius,radius,2*radius), color=(.4,.2,0))


ball = sphere(pos=(0,0,0), velocity=vector(1,1,0))


# callbacks
def keydown(evt):
    s = evt.key

    if s in ['esc', 'q', 'Q']:exit()

scene.bind('keydown',keydown)
# or
# keydown = lambda evt: evt.key in ['esc, 'q', 'Q'] and exit()
# scene.bind('keydown', keydown)
##

dt = 0.1
while true:
    rate(100)
    ball.pos += dt * ball.velocity

    if ball.x < (-width/2 + 2*radius): # left wall
        ball.x = -width/2 + 2*radius
        ball.velocity.x = -ball.velocity.x
    if ball.y > (height/2 - 2*radius):  # top wall
        ball.y = height/2 - 2*radius
        ball.velocity.y = -ball.velocity.y
    if ball.x > (width/2 - 2*radius):
        ball.x = width/2 - 2*radius
        ball.velocity.x = -ball.velocity.x
    if ball.y < (-height/2 + 2*radius): # bottom wall
        ball.y = -height/2 + 2*radius
        ball.velocity.y = -ball.velocity.y
