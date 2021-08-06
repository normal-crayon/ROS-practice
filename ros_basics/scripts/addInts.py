#!/usr/bin/env python3

from __future__ import print_function

from ros_basics.srv import AddInts, AddIntsResponse
import rospy

def handle_add_ints(req):
    print(f'{req.a} + {req.b} = {req.a + req.b}')
    return AddIntsResponse(req.a + req.b)


def add_ints_server():
    rospy.init_node('add_ints', anonymous=True)
    s = rospy.Service('add_ints', AddInts, handle_add_ints)
    print('ready to add ints')
    rospy.spin()


if __name__ == '__main__':
    add_ints_server()
