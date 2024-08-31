from typing import Tuple

from constants.constants import LOOKUP_TABLE_PATH


def parse_mapping_file() -> Tuple[list[str], dict]:
    with open(LOOKUP_TABLE_PATH) as file:
        mapping_data = dict()
        line_no = 1
        for line in file:
            if line_no == 1:
                mapping_metadata = parse_mapping_metadata(line.strip("\n"))
            else:
                mapping_datum_key, mapping_datum_value = parse_mapping_data(line.strip("\n"), mapping_metadata, line_no)
                mapping_data[mapping_datum_key] = mapping_datum_value
            line_no += 1
        return mapping_metadata, mapping_data


def parse_mapping_metadata(record: str) -> list[str]:
    mapping_fields = record.split(",")
    return mapping_fields[:-1]


def parse_mapping_data(record: str, mapping_metadata: list[str], line_no) -> tuple[str, str]:
    record_list = record.split(",")

    if len(record_list) != len(mapping_metadata) + 1:
        raise Exception(f"Mapping File Parsing Action Error: Metadata and actual data does not match. Error in line "
                        f"{line_no}")

    mapping_datum_key = ",".join(record_list[:-1])
    mapping_datum_value = record_list[-1]
    return mapping_datum_key.lower(), mapping_datum_value.lower()
