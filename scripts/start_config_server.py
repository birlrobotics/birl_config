#!/usr/bin/env python

import rospy

from dynamic_reconfigure.server import Server
from birl_config.cfg import MultiModalConfig, HMMConfig

def callback(config, level):
    rospy.loginfo("config: %s, level %s."%(config, level))
    return config

if __name__ == "__main__":
    rospy.init_node("start_birl_config_server", anonymous = True)

    srv = Server(MultiModalConfig, callback, namespace='/birl_config/modality_config')
    srv = Server(HMMConfig, callback, namespace='/birl_config/introspection_model_config/HMM')
    rospy.spin()
