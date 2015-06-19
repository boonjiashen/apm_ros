#!/usr/bin/env python
"""Receives main wind messages and tells mavros to move
in that respective direction"""
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

import geometry_msgs.msg
import std_msgs.msg
import claw_machine.msg

# Maps constant integers (0, 1, etc) to direction strings ('N', 'S', etc)
# So that we can quickly get the strings during the infinite loop
msg_val2key = dict([
        (val, key)
        for key, val in claw_machine.msg.main_wind.__dict__.iteritems()
        if type(val) == int
        ])

def callback(msg):
    direction = msg_val2key[msg.direction]  # String 'N', 'S', etc
    north_vel = ('N' in direction) - ('S' in direction)
    east_vel = ('E' in direction) - ('W' in direction)

    msg = geometry_msgs.msg.TwistStamped()
    msg.header = std_msgs.msg.Header() 
    msg.header.frame_id = ""
    msg.header.stamp = rospy.Time.now()

    msg.twist = geometry_msgs.msg.Twist()
    msg.twist.linear = geometry_msgs.msg.Vector3(
            x=north_vel,
            y=east_vel,
            )
    print (msg)

def manual_control():
    print 'wow'

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("main_wind", claw_machine.msg.main_wind, callback)
    rospy.Publisher("/mavros/setpoint_velocity/cmd_vel",
            geometry_msgs.msg.TwistStamped,
            queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    manual_control()
