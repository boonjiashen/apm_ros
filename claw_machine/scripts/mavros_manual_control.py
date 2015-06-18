#!/usr/bin/env python
"""Receives main wind messages and tells mavros to move
in that respective direction"""
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8
from std_msgs.msg import String
import claw_machine.msg

import sys, select, termios, tty

# Maps constant integers (0, 1, etc) to direction strings ('N', 'S', etc)
# So that we can quickly get the strings during the infinite loop
msg_val2key = dict([
        (val, key)
        for key, val in claw_machine.msg.main_wind.__dict__.iteritems()
        if type(val) == int
        ])

def callback(msg):
    print msg_val2key[msg.direction]

def manual_control():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("main_wind", claw_machine.msg.main_wind, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    manual_control()
