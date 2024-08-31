import argparse
import actions

parser = argparse.ArgumentParser()


if __name__ == "__main__":
    print("Script Execution Started")
    parser.add_argument("-if", "--input", help="Input File Path")
    parser.add_argument("-clf", "--customLogFormat", help="Input File Path")
    cli_args = parser.parse_args()
    actions.execute(cli_args)
    print("Script Execution Ended")
