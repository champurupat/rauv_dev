#!/usr/bin/env python

import rospy
from templates.srv import custom_service, custom_serviceResponse 
# {}.{} import {} (pkg dir name, srv dir, (srv filename, srvfilenameResponse camelCase for items after '---')

def custom_callback(custom_request):
    cust_int_result = custom_request.cust_a * custom_request.cust_b
    cust_dict = {1:"one", 2:"two", 3:"three"}
    cust_str_result = cust_dict[len(str(cust_int_result))]
    return custom_serviceResponse(cust_int_result, cust_str_result)

def custom_multiply_example():
    rospy.init_node("custom_service")
    service = rospy.Service("custom_service", custom_service, custom_callback)
    rospy.spin()

if __name__ == "__main__":
    custom_multiply_example()
