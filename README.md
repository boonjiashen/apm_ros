# apm_ros
Exploratory repo to try out functionality of ROS/Gazebo on a Pixhawk running APM autopilot

## How to run mavros
First run the following. Change USB0 to whatever port the Pixhawk is attached to. This launches `mavros_node`.

    >> roslaunch mavros apm.launch fcu_url:=/dev/ttyUSB0:57600

Then on a new terminal, run the following. This sets mavros' stream rate to be 10 Hz, but also enables the stream of sensor data from mavros. Without it, you may not be able to get Pixhawk's kinematic state, say, if you run `>> rostopic echo /mavros/imu/data`.

    >> rosrun mavros mavsys rate --all 10

## How to run Gazebo simulator of IRIS+

    >> roslaunch px4 gazebo_iris_empty_world.launch 
