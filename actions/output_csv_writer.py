import csv


def write_csv_output(output_file_name: str, counter: dict, metadata: list[str]) -> None:
    with open(output_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(metadata)
        for key, value in counter.items():
            writer.writerow(key.split(",")+[value])

        print("Output file generated at " + output_file_name)
