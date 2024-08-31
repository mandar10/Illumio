# Documentation

## How to start the script
In the root folder of the project, run the following command. The output file will be generated in the output folder within the project's root.

#### Syntax

python main.py -if [input_file] -clf [custom_log_format]


#### Example

python main.py -if /Users/mandarmhapsekar/IdeaProjects/Illumio/test/data/flow_log_sample_1 -clf dstport,protocol


#### Arguments
-if, --input: Path of the input Flow Log file

-clf, --customLogFormat: Custom format for Flow Log file. The fields are Comma Separated. This is not a mandatory field. Use this argument when you don't want to use the default format.


## Code Details

### Design
The program divides the task into different subtasks, which are represented by actions. Each action performs a specific task and gives control to the following action. All the actions are executed sequentially to achieve the goal. Another goal of the program is to achieve code scalability, where the tasks like mapping and counting field combination can be scaled easily without code changes. E.g. adding more fields in the future in the lookup table or in the field combinations.

### Packages
| Package Name | Details                                                                                                                                                                                                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Actions      | This package consists of all the actions that are needed to perform the overall task, like parsing the flow log file, parsing the lookup table, mapping the records, counting the tags and combination fields, and writing the output into a file. |
| Constants    | This package contains the constants required throughout the program. It also contains the lookup table and the number-to-protocol mapping file.                                                                                                    |
| Data         | This package consists of a data class that represents the available fields for the Flow Log. This is referred from the Flow Log AWS Official Documentation, which was shared in the email.                                                         |
| Output       | This package contains all the output file generated.                                                                                                                                                                                               |
| Test         | This package contains all the sample input files that can be used to test the program.                                                                                                                                                             |
| Utils        | This package contains all the helper methods that are used across the program.                                                                                                                                                                     |


### Actions

| Action                  | Details                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------|
| Flow Log Parser         | This action parses the input Flow Log file and generates a list of FlowLog Class objects.           |
| Mapping File Parser     | This action parses the lookup table and generates a dictionary for O(1) mapping.                    |
| Flow Log Counter        | This action counts the frequency for any field combination specified.                               |
| Flow Log Mapper Counter | This action maps the specified fields to the appropriate tags and counts the frequency of the tags. |
| Output CSV Writer       | This action writes the counts to a CSV file                                                         |

Note: The order of the execution can be adjusted in the actions/init.py execute() method


### Using custom format
1. Use the -clf or --customLogFormat argument to specify your custom format. The fields should be space separated.
2. Try the custom format using this command: python main.py -if /Users/mandarmhapsekar/IdeaProjects/Illumio/test/data/flow_log_sample_2 -clf dstport,protocol


### Add more field combinations
1. Add the new field in COMBINATION_FIELDS_LIST_1 in constants.py
2. Add the output name for that field in COMBINATION_FIELDS_METADATA_1 in constants.py
3. Maintain the order.


### Add new column in the lookup table
1. Create a new lookup table with more columns
2. Change the LOOKUP_TABLE_PATH in constants.py
3. Try the constants/flat/lookup_table_scaled.csv for reference


## Testing

| Test Case                                          | Details                                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Valid Flow Log File                                | Testing a Valid Flow Log file                                                                   |
| Valid Flow Log File with Custom Format             | Testing a Valid Flow log file with Custom Format                                                |
| Invalid Flow Log File with missing values in a row | Testing a Invalid Flow log file where 1 record does not have all the fields                     |
| Invalid Flow Log File with Invalid Protocol Number | Testing a Invalid Flow log file where 1 record has a invalid protocol number                    |
| Valid Lookup Table                                 | Testing a Valid Lookup Table                                                                    |
| Valid Lookup Table with additional columns         | Testing a Valid Lookup Table with more columns                                                  |
| Invalid Lookup Table with missing values in a row  | Testing a Invalid Lookup Table where 1 record does not have all the values                      |
| Valid Combination Fields                           | Testing a Valid Combination Field as specified in the requirement                               |
| Invalid Combination Fields                         | Testing a Invalid Combination Field where 1 of the field does not belong to the Flow Log fields |
| Case Insensitive Mapping                           | Testing a Mapping Condition where the values are same but in different case                     |


## Assumptions

1. Lookup Table file first row will be the Flow Logs fields names as mentioned in the Flow Log documentation if not then the system raises an exception.
2. Tag Column in the Lookup Table will be always at the end.
3. Field mentioned in the combination must match to the fields name in the Flow Log documentation if not then the system raises an exception.
4. Two outputs is written to a separate file.