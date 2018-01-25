import ipdb
def get_interested_fields(config):
    ipdb.set_trace()
    [
        ('use_EndpointState_in_multimodal_fusion', [
            '.endpoint_state.pose.position.x',
            '.endpoint_state.pose.position.y',
            '.endpoint_state.pose.position.z',
            '.endpoint_state.pose.orientation.x',
            '.endpoint_state.pose.orientation.y',
            '.endpoint_state.pose.orientation.z',
            '.endpoint_state.pose.orientation.w',
        ]),
        ("use_WrenchStamped_in_multimodal_fusion", [
             '.wrench_stamped.wrench.force.x',
             '.wrench_stamped.wrench.force.y',
             '.wrench_stamped.wrench.force.z',
             '.wrench_stamped.wrench.torque.x',
             '.wrench_stamped.wrench.torque.y',
             '.wrench_stamped.wrench.torque.z',
        ]),
        ("use_JointState_in_multimodal_fusion", [
        ]),
    ]
    print config
    pass
