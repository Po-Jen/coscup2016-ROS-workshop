#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('topic_name', String, queue_size=10)
    rospy.init_node('publisher_node_name')
    rate = rospy.Rate(10) # 10hz 
    while not rospy.is_shutdown():
        str_to_be_pub = "welcome to coscup %s" %rospy.get_time()
        pub.publish(str_to_be_pub)
        rate.sleep()  

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

