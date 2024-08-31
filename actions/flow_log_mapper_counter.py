from collections import defaultdict

from data.flow_log_dataclass import FlowLog


def map_flow_log_data(flow_log_dataclass_list: list[FlowLog], mapping_metadata: list[str], mapping_data: dict):
    counter = defaultdict(int)
    for flow_log_dataclass in flow_log_dataclass_list:
        key = ""
        for metadata in mapping_metadata:
            key += getattr(flow_log_dataclass, metadata, "") + ","

        tag = "Untagged"
        if key[:-1] in mapping_data:
            tag = mapping_data[key[:-1]]
        counter[tag] += 1
    return counter
