#!/usr/bin/env python

import rospy
from coscup_2_topic.msg import Num

def talker():
    pub = rospy.Publisher('my_msg_topic_name', Num, queue_size=10)
    rospy.init_node('my_msg_publisher_node_name')
    rate = rospy.Rate(10) # 10hz 
    
    #Num is a type
    message = Num()
    message.num=0
    
    while not rospy.is_shutdown():
	message.num += 1	
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

