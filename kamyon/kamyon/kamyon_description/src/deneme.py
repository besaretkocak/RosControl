<?xml version="1.0"?>
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include "std_msgs/Float64.h"

class controller {
    public:
    controller() {
        sub= n.subscribe("/kamyon/joint1_position_controller/command",1000, &controller::callback, this);
        sub= n.subscribe("/kamyon/joint2_position_controller/command",1000, &controller::callback, this);
        sub= n.subscribe("/kamyon/joint3_position_controller/command",1000, &controller::callback, this);
        sub= n.subscribe("/kamyon/joint4_position_controller/command",1000, &controller::callback, this);
        pub= n.advertise<std_msgs::String>("anotherTopic",1000);

    }

void callback(const std_msgs::Float64::ConstPtr& msg) {
std_msgs::String pub_str;
std:: stringstream ss;

ss<<"controller heard:" << msg->data.c_str();

pub_str.data == ss.str();
std::cout <<pub_str.data.c_str() <<std::endl;
pub.publish(pub_str);
}
private:
ros::NodeHandle n;
ros::Subscriber sub;
ros:: Publisher pub;
 
};

int main(int argc, char **ardv){
ros:: init(argc,argv,"controller");
controller ctrl;
ros::spin();
}

