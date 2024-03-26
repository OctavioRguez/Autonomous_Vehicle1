# Autonomous Vehicle

## Description
The Autonomous Vehicle package is a ROS-based software package designed for autonomous navigation. 

It includes modules for sensor image processing, object detection and classification, control, and line following. 
This package aims to provide a comprehensive solution for autonomous vehicles development.

## Installation

### Dependencies
The following Python libraries are used:
- OpenCV
- CV_Bridge
- Numpy
- Rospy

Additionally the following ROS messages are used:
- std_msgs (String, Float32)
- sensor_msgs (Image)
- geometry_msgs (Twist)


### Building
```bash
cd ~/catkin_ws/src
git clone https://github.com/OctavioRguez/Autonomous_Vehicle.git
cd ..
mv ./Autonomous_Vehicle ./autonomous_vehicle
catkin_make
```

## Launch
For running the project, you can use the following command:
```bash
    roslaunch autonomous_vehicle puzzlebot.launch
```

## License
This project is licensed under the BSD 3-Clause License. See the LICENSE file for details.
