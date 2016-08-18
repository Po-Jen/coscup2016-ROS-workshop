#!/usr/bin/env python
import rospy

if __name__ == '__main__':
    try:
        rospy.init_node('my_first_node')
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

