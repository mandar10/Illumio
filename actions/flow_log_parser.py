import os
import csv

from constants.constants import DEFAULT_LOG_FORMAT, NUMBER_TO_PROTOCOL_MAPPER_FILE_PATH
from data.flow_log_dataclass import FlowLog
from utils import common_utils


def parse_flow_log_file(input_file: str, custom_log_format: str) -> list[FlowLog]:
    if input_file == "" or not os.path.exists(input_file):
        raise Exception(f"Flow Log Parsing Action Error: Error in the input file {input_file}. File does not exist or is invalid")

    with open(input_file) as file:
        flow_log_dataclass_list = list()
        line_no = 1
        for line in file:
            number_to_protocol_mapper = create_number_to_protocol_mapper()
            flow_log_dataclass = parse_flow_log_record(line.strip("\n"), custom_log_format, number_to_protocol_mapper, line_no)
            flow_log_dataclass_list.append(flow_log_dataclass)
            line_no += 1

        return flow_log_dataclass_list


def create_number_to_protocol_mapper() -> dict:
    try:
        number_to_protocol_mapper = dict()
        with open(NUMBER_TO_PROTOCOL_MAPPER_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                number_to_protocol_mapper[row[0]] = row[1]
        return number_to_protocol_mapper
    except Exception as e:
        raise Exception(f"Flow Log Parsing Action Error: Error in Number to Protocol Mapping CSV file") from e


def parse_flow_log_record(record: str, custom_log_format: str, number_to_protocol_mapper: dict, line_no: int) -> FlowLog:
    record_list = record.split()
    if custom_log_format is not None:
        log_format_list = custom_log_format.split(",")
    else:
        log_format_list = DEFAULT_LOG_FORMAT.split(",")

    if len(record_list) != len(log_format_list):
        raise Exception(f"Flow Log Parsing Action Error: The input file format does not match with default/custom "
                        f"format. Error on line {line_no} in the input file")

    flow_log_dict = dict()
    for i in range(len(log_format_list)):
        if log_format_list[i] == "protocol":
            if record_list[i] in number_to_protocol_mapper:
                record_list[i] = number_to_protocol_mapper[record_list[i]].lower()
            else:
                raise Exception(f"Flow Log Parsing Action Error: Error on line {line_no} in the input file. Number to "
                                f"Protocol Mapping failed")
        flow_log_dict[log_format_list[i].replace("-", "_").strip()] = record_list[i]

    return common_utils.class_from_args(FlowLog, flow_log_dict)
