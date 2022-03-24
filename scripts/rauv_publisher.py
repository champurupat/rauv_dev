#!/usr/bin/env python

import rospy
from templates.msg import rauv_template # {}.{} import {} (pkg dir name, msg dir, filename of msg)

def rauv_speak():
    pub = rospy.Publisher("custom_topic", rauv_template, queue_size=10)
    rospy.init_node("rauv_pub_template", anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("running rauv publisher template")
    while not rospy.is_shutdown():
        msg = rauv_template()
        msg.cust_string = 'hello world'
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        rauv_speak()
    except rospy.ROSInterruptException:
        pass
