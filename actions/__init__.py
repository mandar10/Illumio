from actions.flow_log_counter import count_flow_log_data_field_combinations
from actions.flow_log_mapper_counter import map_flow_log_data
from actions.flow_log_parser import parse_flow_log_file
from actions.mapping_file_parser import parse_mapping_file
from actions.output_csv_writer import write_csv_output
from constants.constants import COMBINATION_FIELDS_LIST_1, COUNT_OF_TAGS_METADATA, COMBINATION_FIELDS_METADATA_1


def execute(cli_args):
    # Parsing the Flow Log Data
    flow_log_dataclass_list = parse_flow_log_file(cli_args.input, cli_args.customLogFormat)

    # Parse the Lookup Table/Mapping File
    mapping_metadata, mapping_data = parse_mapping_file()

    # Map and Count the Tags
    flow_log_data_field_combination_counts = count_flow_log_data_field_combinations(COMBINATION_FIELDS_LIST_1,
                                                                                    flow_log_dataclass_list)

    # Count the field combinations
    flow_log_data_mapping_counts = map_flow_log_data(flow_log_dataclass_list, mapping_metadata, mapping_data)

    # Generate the output file
    write_csv_output("output/output_count_of_tags.csv", flow_log_data_mapping_counts, COUNT_OF_TAGS_METADATA)
    write_csv_output("output/output_count_of_combination_fields.csv", flow_log_data_field_combination_counts,
                     COMBINATION_FIELDS_METADATA_1)
