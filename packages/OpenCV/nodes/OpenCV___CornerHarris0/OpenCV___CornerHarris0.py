from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class CornerHarris_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(CornerHarris_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_unCornerHarris = None
        self.img_CornerHarris = None
        self.img_grayed=None

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unCornerHarris = self.input(0)
        self.img_grayed=cv2.cvtColor(self.img_unCornerHarris,cv2.COLOR_BGRA2GRAY)
        blocksize = self.input(1)
       # blocksize=int(blocksize)
        arpertureSize=self.input(2)
       # arpertureSize=int(arpertureSize)
        k=self.input(3)
      #  k=int(k)
      
        
        self.img_CornerHarris = cv2.cornerHarris( self.img_grayed,blocksize,arpertureSize,k)
        self.main_widget.show_image(self.img_CornerHarris)
        self.outputs[0].set_val(self.img_CornerHarris)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
