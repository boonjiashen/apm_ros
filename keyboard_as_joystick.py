"""ROS node that takes keystrokes and publishes
them to a topic

Meant to emulate an 8-directional arcade joystick
"""

import pygame
from pygame.locals import *  
      
def talker():

    # Initializing Pygame stuff
    pygame.init()
    screen=pygame.display.set_mode((640,480),0,24)
    pygame.display.set_caption("Key Press Test")
    f1=pygame.font.SysFont("comicsansms",24)
      
    # Initialize ROS stuff
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        event = pygame.event.poll()
        if event.type == pygame.NOEVENT:
            continue
        if event.type == pygame.QUIT:
            break
        if not pygame.key.get_focused():
            continue

        names = [pygame.key.name(i)
                for i, is_pressed in enumerate(pygame.key.get_pressed())
                if is_pressed]
        if 'escape' in names:
            break

        ys = [100 * i for i in range(1, 1 + len(names))]
        screen.fill((255,255,255))
        for name, y in zip(names, ys):
            text = f1.render(name, True, (0, 0, 0))
            screen.blit(text, (100, y))

        pygame.display.update()
        
def talker():
    while not :
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass