DEFAULT_LOG_FORMAT = "version,account-id,interface-id,srcaddr,dstaddr,srcport,dstport,protocol,packets,bytes,start," \
                     "end,action,log-status"

COUNT_OF_TAGS_METADATA = ["Tag", "Count"]

COMBINATION_FIELDS_METADATA_1 = ["Port", "Protocol", "Count"]
COMBINATION_FIELDS_LIST_1 = ["dstport", "protocol"]

LOOKUP_TABLE_VALID_PATH = "constants/flat/lookup_table.csv"
LOOKUP_TABLE_CASE_INSENSITIVE_PATH = "test/data/lookup_table_case_insensitive.csv"
LOOKUP_TABLE_INVALID_PATH = "test/data/lookup_table_invalid_2.csv"

NUMBER_TO_PROTOCOL_MAPPER_FILE_PATH = "constants/flat/protocol_numbers.csv"
