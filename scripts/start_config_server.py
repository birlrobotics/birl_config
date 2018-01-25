#!/usr/bin/env python

import rospy
import json
import os
import ipdb
import copy

dir_of_this_script = os.path.dirname(os.path.realpath(__file__))

def get_json_path(cfg_name):
    json_path = os.path.join(
        dir_of_this_script,
        '..',
        'cfg',
        '%s.json'%cfg_name,
    )
    return json_path

def safe_update_dict(a, b):
    for key in b:
        if key in a:
            if type(a[key]) == type(b[key]):
                if type(a[key])==dict: 
                    safe_update_dict(a[key], b[key])
                else:
                    a[key]=b[key]
             

def update_old_config_if_exists(server, cfg_name):
    json_path = get_json_path(cfg_name)
    if os.path.isfile(json_path):
        try:
            old_config = json.load(open(json_path, 'r'))
            now_config = copy.deepcopy(server.config)
            safe_update_dict(now_config, old_config) 
            server.update_configuration(now_config)
        except IOError as e:
            print "Reading json config failed, I/O error({0}): {1}".format(e.errno, e.strerror)

latest_config_dict = {}
def cb_gen(cfg_name):
    def callback(config, level):
        global latest_config_dict
        rospy.loginfo("config: %s, level %s."%(config, level))
        latest_config_dict[cfg_name] = config
        return config
    return callback

if __name__ == "__main__":
    from dynamic_reconfigure.server import Server
    from birl_config.cfg import MultiModalConfig, hmmlearnConfig, bnpyConfig

    rospy.init_node("start_birl_config_server", anonymous = True)

    server_dict = {}

    server_dict["MultiModalConfig"] = Server(MultiModalConfig, cb_gen("MultiModalConfig"), namespace='/birl_config/modality_config')
    server_dict["hmmlearnConfig"] = Server(hmmlearnConfig, cb_gen("hmmlearnConfig"), namespace='/birl_config/introspection_model_config/HMM/hmmlearn')
    server_dict["bnpyConfig"] = Server(bnpyConfig, cb_gen("bnpyConfig"), namespace='/birl_config/introspection_model_config/HMM/bnpy')

    for cfg_name in server_dict:
        update_old_config_if_exists(
            server_dict[cfg_name],
            cfg_name,
        )

    rospy.spin()

    for cfg_name in latest_config_dict:
        json_path = get_json_path(cfg_name)
        try:
            json.dump(
                latest_config_dict[cfg_name],
                open(json_path, 'w'),
            )
        except IOError as e:
            print "Saving json config failed, I/O error({0}): {1}".format(e.errno, e.strerror)
        

