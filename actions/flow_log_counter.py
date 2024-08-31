from collections import defaultdict

from data.flow_log_dataclass import FlowLog


def count_flow_log_data_field_combinations(combination_list: list[str], flow_log_dataclass_list: list[FlowLog]) -> dict:
    counter = defaultdict(int)
    for flow_log_dataclass in flow_log_dataclass_list:
        key = ""
        for combination in combination_list:
            key += getattr(flow_log_dataclass, combination, "") + ","

        counter[key[:-1]] += 1

    return counter
