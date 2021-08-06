#!/usr/bin/env python3

import sys
import rospy 
from ros_basics.srv import *

def add_ints_client(x, y):
    rospy.wait_for_service('add_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_ints', AddInts)
        res1 = add_two_ints(x, y)
        return res1.sum

    except rospy.ServiceException as e:
        print('service call failed', e)


def usage():
    return f'{sys.argv[0]}[x y]'

if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)

    print(f'requesting {x} + {y}')
    print(f'{x} + {y} = {add_ints_client(x, y)}')
