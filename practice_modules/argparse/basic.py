import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    return parser.parse_args()

def main():

    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    print(input_path)
    print(output_path)

if __name__ == "__main__":
    main()