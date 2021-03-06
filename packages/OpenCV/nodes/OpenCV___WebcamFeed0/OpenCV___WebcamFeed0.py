from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class WebcamFeed_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(WebcamFeed_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.log = self.new_log('Webcam Feed log')

        self.initialized()

    def video_picture_updated(self, img):
        self.log.log('video picture updated')
        self.outputs[0].set_val(img)
        # self.update()


    def update_event(self, input_called=-1):
        pass  # no central updating here

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...



    # optional - important for threading - stop everything here
    def removing(self):
        self.log_message('Webcam feed node instance successfully removed. Have a good day.', target='global')
