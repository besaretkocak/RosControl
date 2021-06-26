#!/usr/bin/env python3

from __future__ import print_function

import threading

import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

wheel_1speed = rospy.Publisher('/kamyon/joint1_position_controller/command', Float64, queue_size=10)
wheel_2speed = rospy.Publisher('/kamyon/joint2_position_controller/command', Float64, queue_size=10)
wheel_3speed = rospy.Publisher('/kamyon/joint13position_controller/command', Float64, queue_size=10)
wheel_4speed = rospy.Publisher('/kamyon/joint4_position_controller/command', Float64, queue_size=10)
kasa = rospy.Publisher('/kamyon/joint5_position_controller/command', Float64, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1000) # 10hz


def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

   
if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    key_timeout = rospy.get_param("~key_timeout", 0.0)

  
    stand = 0.0
    wheel1_speed = 0.0
    wheel2_speed = 0.0
    wheel3_speed = 0.0
    wheel4_speed = 0.0
    

    if key_timeout == 0.0:
        key_timeout = None
    try:
        while not rospy.is_shutdown():
            key = getKey(key_timeout)

            if(key=="r"):
                if not stand < 0:
                    stand = stand- 0.05 #0.5 - -0.5
            if(key=="f"):
                if not stand > 1.11:
                    stand = stand + 0.05 #0.5 - -0.5
            if(key=="a"):
              
                    wheel1_speed = wheel1_speed + 500
                    wheel2_speed = wheel2_speed + 500
                    wheel3_speed = wheel3_speed - 500
                    wheel4_speed = wheel4_speed - 500
                 
          
            if(key=="d"):
           
                    wheel1_speed = wheel1_speed - 500
                    wheel2_speed = wheel2_speed - 500
                    wheel3_speed = wheel3_speed + 500
                    wheel4_speed = wheel4_speed + 500
  
                
            if(key=="w"):
              
                    wheel1_speed = wheel1_speed + 500
                    wheel2_speed = wheel2_speed + 500
                    wheel3_speed = wheel3_speed + 500
                    wheel4_speed = wheel4_speed + 500
                 
          
            if(key=="s"):
           
                    wheel1_speed = wheel1_speed - 500
                    wheel2_speed = wheel2_speed - 500
                    wheel3_speed = wheel3_speed - 500
                    wheel4_speed = wheel4_speed - 500
          	  
            print(key + " v:{:.2f} s:{:.1f}   ".format(wheel1_speed,stand))


            #rospy.loginfo(fork_base_pos)
            wheel_1speed.publish(wheel1_speed) 
            wheel_2speed.publish(wheel2_speed)         
            wheel_3speed.publish(wheel3_speed)
            wheel_4speed.publish(wheel4_speed)
            kasa.publish(stand)         
            rate.sleep()

            if (key == '\x03'):
                break
    
    except Exception as e:
        print(e)

    finally:        
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
