import Rosbag_Analysis as ra
import numpy as np

# Main function for calling rosbag analysis methods
# --> is gonna be replaced by (or integrated) in GUI script 

array_objectIDs = ra.Rosbag_Analysis.getObjectIDs('../bagfiles/Objektliste_2020-5-4-13-7-21.bag')
print(array_objectIDs)

# generic implementation (in work) 
                                                                                                        #bag file                #object id    #category      #attribute
(array_timestamps, array_values_x) = ra.Rosbag_Analysis.getRawData('../bagfiles/Objektliste_2020-5-4-13-7-21.bag', 2, "dimension", "length")
(array_timestamps, array_values_y) = ra.Rosbag_Analysis.getRawData('../bagfiles/Objektliste_2020-5-4-13-7-21.bag', 0, "classification", "car")

#prototype
#(array_timestamps, array_values_difference) = ra.Rosbag_Analysis.getAdvancedData('../bagfiles/Objektliste.bag', '../bagfiles/Objektliste.bag', 0, 1, "dimension", "width", "difference")


#deprecated:
# example: getting geometric.x values for simple plot
x_array_obj1 = []   # array of all x values of object 1
(timestamps1, x_array_obj1) = ra.Rosbag_Analysis.get_geometric_x('../bagfiles/Objektliste.bag', 1)


### for showing the arrays

print("Printing values out of generic function: ")
for i in range(0, len(array_values_x), 1):
    print(array_values_x[i])
    
#print("Printing  values out of generic function: ")
#for i in range(0, len(array_values_y), 1):
#    print(array_values_y[i])

#print("Printing  values out of advanced function - difference: ")
#for i in range(0, len(array_values_difference), 1):
#    print(array_values_difference[i])
  
# for calculating differnces between arrays:
  
#diff = []
#diff = np.subtract(x_array_obj1, x_array_obj2)
#print(diff)
