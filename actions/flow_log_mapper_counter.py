from collections import defaultdict

from data.flow_log_dataclass import FlowLog


def map_flow_log_data(flow_log_dataclass_list: list[FlowLog], mapping_metadata: list[str], mapping_data: dict) -> dict:
    counter = defaultdict(int)
    for flow_log_dataclass in flow_log_dataclass_list:
        key = ""
        for metadata in mapping_metadata:
            if not getattr(flow_log_dataclass, metadata.replace("-", "_"), None) is None:
                key += getattr(flow_log_dataclass, metadata.replace("-", "_")) + ","
            else:
                raise Exception(f"Mapper Counter Action Error: Lookup Table Column does not match with any of the "
                                f"Flow Log fields. Error in column - {metadata}")

        tag = "Untagged"
        if key[:-1].lower() in mapping_data:
            tag = mapping_data[key[:-1].lower()]
        counter[tag] += 1
    return counter
