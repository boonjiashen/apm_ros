#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8
from std_msgs.msg import String

import sys, select, termios, tty

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
anything else : stop

CTRL-C to quit
"""

char2dir = {
	'u': 'NW',
	'i': 'N',
	'o': 'NE',
	'j': 'W',
	'k': 'X',
	'l': 'E',
	'm': 'SW',
	',': 'S',
	'.': 'SE',
}

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

speed = .5
turn = 1

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

def keyboard():
    settings = termios.tcgetattr(sys.stdin)
    
    pub = rospy.Publisher('main_wind', String, queue_size=10)
    rospy.init_node('teleop_twist_keyboard')
    rate = rospy.Rate(10) # 10hz

    x = 0
    th = 0
    status = 0

    try:
        print msg
        print 'dawg'
        print 'son'
        while not rospy.is_shutdown():
            key = getKey()
            print key
            if key == '\x03':
            	break
            pub.publish(key)
            rate.sleep()
        print 'hi'

    except Exception as e:
        print e

    finally:
        pub.publish('dayum')

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)


    try:
        keyboard()
    except rospy.ROSInterruptException:
        pass