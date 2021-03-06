from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class YUV_I420_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(YUV_I420_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_unYUV_I420 = None
        self.img_YUV_I420 = None

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unYUV_I420 = self.input(0)
      
        self.img_YUV_I420 = cv2.cvtColor(self.img_unYUV_I420,cv2.COLOR_BGRA2YUV_I420)
        #self.cnvt=cv2.imshow('gray_image',self.img_YUV_I420)
        self.main_widget.show_image(self.img_YUV_I420)
        self.outputs[0].set_val(self.img_YUV_I420)

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
