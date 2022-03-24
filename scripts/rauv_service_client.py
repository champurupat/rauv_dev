#!/usr/bin/env python
import rospy
from templates.srv import custom_service, custom_serviceResponse # {}.{} import {} (pkg dir name, srv dir, (srv filename, srvfilenameResponse camelCase for items after '---') 

def custom_client(x, y):
    rospy.init_node("custom_client_node")
    rospy.wait_for_service("custom_service")
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        multiply_example = rospy.ServiceProxy("custom_service", custom_service)
        response = multiply_example(x, y)
        rospy.loginfo(response.cust_result)
        rate.sleep()

if __name__ == "__main__":
    try:
        custom_client(2,8)
    except rospy.ServiceException as e:
        print("Service call failed %s", e)

