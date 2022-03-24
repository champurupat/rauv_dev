#!/usr/bin/python

import rospy
from templates.msg import rauv_template # {}.{} import {} (pkg dir name, msg dir name, filename) 

def main():
    this_object = CustomMsg()
    rospy.init_node("custom_subscriber", anonymous=False)
    # rospy.Subscriber('custom_topic', rauv_template, callback, queue_size=10)
    rospy.Subscriber('custom_topic', rauv_template, this_object.custom_callback, queue_size=10)
    rospy.spin()

class CustomMsg(object):
    def __init__(self):
        pass

    def custom_callback(self, msg):
        rospy.loginfo("listening: {},{}".format(msg.cust_x, msg.cust_string))

# def callback(msgg):
#     rospy.loginfo("listening: {},{}".format(msgg.cust_x, msgg.cust_string))
     
if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
