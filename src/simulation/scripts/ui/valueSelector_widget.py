'''
    this small widget is shown in plot dialog
    here the user can select which of the values 
    he wants to plot
'''
from python_qt_binding import QtCore, QtGui
from python_qt_binding.QtWidgets import *
from object_list_msg import obj_list_msg

class ValueSelectorWidget(QGroupBox):
    
    def __init__(self, parent=None, hasObjCnt=True):
        super(ValueSelectorWidget, self).__init__()
        self.parent = parent
        self.hasObjCnt = hasObjCnt
        
        self.layout = QVBoxLayout()
        self.setTitle('Select Value')
        self.valueTreeWidget = QTreeWidget()
        self.buildTree()
        self.layout.addWidget(self.valueTreeWidget)
        self.setLayout(self.layout)
        
    def buildTree(self):
        '''
            fills the treeWidget
            according to the structure of ObjectList.msg
        '''
        for key in obj_list_msg:
            category = QTreeWidgetItem(self.valueTreeWidget)
            category.setText(0, key)
            for att in obj_list_msg[key]:
                attribute = QTreeWidgetItem(category)
                attribute.setText(0, att)
        
        if self.hasObjCnt:        
            # add object_count
            category = QTreeWidgetItem(self.valueTreeWidget)
            category.setText(0, 'object_count')
    
            
    def getAttribute(self):
        currentItem = self.valueTreeWidget.currentItem()
        if currentItem.childCount() == 0: # selctedItem is a attribute
            return currentItem.text(0)
        else: # selected Item is not an attribute
            return ""
    
    def getCategory(self):
        currentItem = self.valueTreeWidget.currentItem()
        if currentItem.childCount() == 0: # selctedItem is a attribute
            return currentItem.parent().text(0)
        else: # selected Item is not an attribute
            return ""
        
    def getCatAndAtt(self):
        '''
            returns the current selected category and attribute
            of the object list message
            if no or an invalid attribute is selected the function
            raises an exception
        '''
        currentItem = self.valueTreeWidget.currentItem()
        
        # if no item at all in the tree is selected
        if currentItem == None:
            raise Exception('No attribute selected! Please select a valid attribute.')
        
        if currentItem.childCount() == 0: # selctedItem is on the lowest layer
            selectedAttribute = currentItem.text(0)
            
            if (selectedAttribute == "prop_existence" or 
            selectedAttribute == "prop_mov" or
            selectedAttribute == "obj_id" or
            selectedAttribute == "object_count" or 
            selectedAttribute == "covariance"):
                selectedCategory = "" 
            else:
                selectedCategory = currentItem.parent().text(0)
                
        else: # selected Item is not an attribute
            selectedAttribute = ""
            selectedCategory = ""
            
        return { 'category' : selectedCategory, 
                'attribute' : selectedAttribute }
        
                

        
        
