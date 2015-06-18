#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8
from std_msgs.msg import String
import claw_machine.msg

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
    
    pub = rospy.Publisher('main_wind', claw_machine.msg.main_wind, queue_size=10)
    rospy.init_node('keyboard', anonymous=True)
    rate = rospy.Rate(30) # 10hz

    try:
        while not rospy.is_shutdown():
            key = getKey()
            if key == '\x03':  # Break at CTRL+C
            	break
            if key not in char2dir:  # ignore unexpected keystrokes
                continue

            direction = char2dir[key]  # string
            msg = getattr(claw_machine.msg.main_wind, direction)  # uint8
            pub.publish(msg)
            rate.sleep()

    except Exception as e:
        print e
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)

    try:
        keyboard()
    except rospy.ROSInterruptException:
        pass
