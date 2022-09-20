import rospy
from sensor_msgs.msg import MagneticField
from datetime import datetime


def callback(imu_msg, mag_msg):
    print("in the callback")
    data = {
        "mag": [mag_msg.magnetic_field.x,
                mag_msg.magnetic_field.y,
                mag_msg.magnetic_field.z
                ],


    }


def MAG_Collector():
    # rospy.init_node('imu_logger_node', anonymous=True)
    odom_sub = rospy.Subscriber(
        '/stm32/mag', MagneticField, callback)
    rospy.spin()
