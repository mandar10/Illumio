from dataclasses import dataclass


@dataclass
class FlowLog:
    # Version 2 Fields
    version: str = None
    account_id: str = None
    interface_id: str = None
    srcaddr: str = None
    dstaddr: str = None
    srcport: str = None
    dstport: str = None
    protocol: str = None
    packets: str = None
    bytes: str = None
    start: str = None
    end: str = None
    action: str = None
    log_status: str = None

    # Version 3 Fields
    vpc_id: str = None
    subnet_id: str = None
    instance_id: str = None
    tcp_flags: str = None
    type: str = None
    pkt_srcaddr: str = None
    pkt_dstaddr: str = None

    # Version 4 Fields
    region: str = None
    az_id: str = None
    sublocation_type: str = None
    sublocation_id: str = None

    # Version 5 Fields
    pkt_src_aws_service: str = None
    pkt_dst_aws_service: str = None
    flow_direction: str = None
    traffic_path: str = None

    # Version 7 Fields
    ecs_cluster_arn: str = None
    ecs_cluster_name: str = None
    ecs_container_instance_arn: str = None
    ecs_container_instance_id: str = None
    ecs_container_id: str = None
    ecs_second_container_id: str = None
    ecs_service_name: str = None
    ecs_task_definition_arn: str = None
    ecs_task_arn: str = None
    ecs_task_id: str = None
