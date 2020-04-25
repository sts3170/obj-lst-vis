#!/usr/bin/env python
import roslib; roslib.load_manifest('visualization_marker_tutorials')
import rospy
from std_msgs.msg import String
from object_list.msg import ObjectsList
from object_list.msg import ObjectList

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math

topic = 'visualization_marker_array'
publisher = rospy.Publisher(topic, MarkerArray,queue_size=10)
rospy.init_node('Objekt_Visualization')

#define each color to the specific class, input value ist the name(string) from the classifciation
def evaluateColor(Class): 
    class_List = {
	"car": [1,0,0,1],
	"truck":[0,1,0,1],
	"motorcycle": [0,0,1,1],
	"bicycle": [1,1,0,1],
	"pedestrian": [1,0,1,3],
	"stacionary": [0,1,1,3],
	"other":[1,1,1,2]   
    }
    return class_List.get(Class)
    
 
def evaluateClassification(objectClass):
    
    temp_prop = 0
    result = ""
    #tmp includes all Attributes of the message Classification
    tmp = [a for a in dir(objectClass) if not a.startswith('__') and not a.startswith('_') and not callable(getattr(objectClass,a))]
    

    for i in range(len(tmp)):
        if(getattr(objectClass, tmp[i]) > temp_prop ):
            temp_prop = getattr(objectClass, tmp[i])
            result = tmp[i]
    return (result) # return value is the name of the class whith the highest probability
            
    


def evaluateObject(objectData):
    marker = Marker()
    r, g, b, typ = evaluateColor(evaluateClassification(objectData.classification))
    marker.header.frame_id = "/obj_vis"
    #marker.type = marker.CUBE
    marker.type = typ
    #rospy.loginfo(typ)
    marker.action = marker.ADD
    marker.scale.x = objectData.dimension.length
    marker.scale.y = objectData.dimension.width
    
    marker.scale.z = objectData.dimension.height
    marker.color.a = 1.0
   
    marker.color.r = r
    marker.color.g = g
    marker.color.b = b
    
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = objectData.geometric.x 
    marker.pose.position.y = objectData.geometric.y * (-1)
    marker.pose.position.z = objectData.dimension.height/2
    #marker.id =0
    return marker

def callback(data):
   
    markerArray = MarkerArray()
    rospy.loginfo(data.obj_list[0].geometric)
    for i in range(len(data.obj_list)):
        markerObj = evaluateObject(data.obj_list[i])
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.obj_list[i])
        markerObj.id = i
        markerArray.markers.append(markerObj)

    publisher.publish(markerArray)
   
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    

    #rospy.Subscriber("chatter", String, callback)
    rospy.Subscriber("camera_obj", ObjectsList, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
