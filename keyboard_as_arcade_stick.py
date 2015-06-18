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

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def keyboard():
    settings = termios.tcgetattr(sys.stdin)
    
    pub = rospy.Publisher('main_wind', String, queue_size=10)
    rospy.init_node('teleop_twist_keyboard')
    rate = rospy.Rate(30) # 10hz

    try:
        print msg
        print 'dawg'
        print 'son'
        while not rospy.is_shutdown():
            key = getKey()
            print key
            if key == '\x03':  # Break at CTRL+C
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
