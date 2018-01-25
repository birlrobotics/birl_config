#!/usr/bin/env python

import rospy
import dynamic_reconfigure.client
from birl_config_parser.config_parser import (
    get_interested_fields,
)

def callback(config):
    rospy.loginfo("Config set to {int_param}, {double_param}, {str_param}, {bool_param}, {size}".format(**config))

if __name__ == "__main__":
    rospy.init_node("test_config_parser")

    try:
        client = dynamic_reconfigure.client.Client("/birl_config/modality_config", timeout=1)
        config = client.get_configuration()
        get_interested_fields(config)
    except rospy.exceptions.ROSException as e:
        rospy.logerr("Have you started dynamic reconfigure server?")
        raise e 
    
