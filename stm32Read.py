import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField
import message_filters

import math
# import Queue
# imuList = Queue.Queue(maxsize=10000)
# magList = Queue.Queue(maxsize=10000)
imuList = list()
magList = list()


def imuCallback(msg):
    global imuList
    result = [
        msg.linear_acceleration.x/9.8,
        msg.linear_acceleration.y/9.8,
        msg.linear_acceleration.z/9.8,
        msg.angular_velocity.x/180*math.pi,
        msg.angular_velocity.y/180*math.pi,
        msg.angular_velocity.z/180*math.pi
    ]
    imuList.append(result)


def magCallback(msg):
    global magList
    result = [
        msg.magnetic_field.x*1e6,
        msg.magnetic_field.y*1e6,
        msg.magnetic_field.z*1e6
    ]
    magList.append(result)


def readACCGYR(entryNum=None):
    global imuList

    del imuList[:]

    if entryNum == None:
        entryNum = 1
    else:
        pass

    imu_sub = rospy.Subscriber("/stm32/imu", Imu, imuCallback)

    # while(result is None):
    #     try:
    #         msg = rospy.wait_for_message("/stm32/imu", Imu, timeout=1)

    #     except:
    #         print("fail")
    #         continue

    # # return [acc, gyr]
    if len(imuList) < entryNum:
        rospy.sleep(1)

    return imuList[0]


def readMAG(entryNum=None):
    global magList
    del magList[:]

    if entryNum == None:
        entryNum = 1
    else:
        pass

    mag_sub = rospy.Subscriber("/stm32/mag", Imu, magCallback)

    # while(result is None):
    #     try:
    #         msg = rospy.wait_for_message(
    #             "/stm32/mag", MagneticField, timeout=1)

    #         result = [
    #             msg.magnetic_field.x*1e6,
    #             msg.magnetic_field.y*1e6,
    #             msg.magnetic_field.z*1e6
    #         ]
    #     except:
    #         print("fail")
    #         continue

    # return [mag]
    if len(magList) < entryNum:
        rospy.sleep(1)

    return magList[0]
    pass
