#!/usr/bin/env python
"""Receives main wind messages and tells mavros to move
in that respective direction"""
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

import geometry_msgs.msg
import std_msgs.msg
import claw_machine.msg

class ManualControl(object):

    # Maps constant integers (0, 1, etc) to direction strings ('N', 'S', etc)
    # So that we can quickly get the strings during the infinite loop
    msg_val2key = dict([
            (val, key)
            for key, val in claw_machine.msg.main_wind.__dict__.iteritems()
            if type(val) == int
            ])
    pub = None  # publisher object whose publish() method publishes

    def callback(self, msg):
        direction = self.msg_val2key[msg.direction]  # String 'N', 'S', etc
        north_vel = ('N' in direction) - ('S' in direction)
        east_vel = ('E' in direction) - ('W' in direction)
        magnitude = 10  # in meters/sec

        msg = geometry_msgs.msg.TwistStamped()

        # We only define `stamp` in header because it's the only
        # member of header used in setpoint_velocity/cmd_vel.
        # `seq` is automatically generated
        msg.header = std_msgs.msg.Header() 
        msg.header.stamp = rospy.Time.now()  

        msg.twist = geometry_msgs.msg.Twist()
        msg.twist.linear = geometry_msgs.msg.Vector3(
                x=magnitude * north_vel,
                y=magnitude * east_vel,
                )

        self.pub.publish(msg)

    def __init__(self):
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber("main_wind", claw_machine.msg.main_wind, self.callback)

        self.pub = rospy.Publisher("/mavros/setpoint_velocity/cmd_vel",
                geometry_msgs.msg.TwistStamped,
                queue_size=10)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    ManualControl()
