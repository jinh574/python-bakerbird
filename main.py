import argparse

from utils import load_input_data, save_output_data, load_input_data_stream
from baker_bird import BakerBird

# 실행 매개변수 Parsing
parser = argparse.ArgumentParser(description="Baker-bird algorithm implemented")
parser.add_argument("input", type=str,
                    help="Input txt file path")
parser.add_argument("output", type=str,
                    help="Output txt file path")
args = parser.parse_args()

if __name__ == "__main__":
    pattern_len, text_len, stream = load_input_data_stream(args.input)
    bb = BakerBird(stream, pattern_len)
    result = bb(stream, text_len)
    save_output_data(args.output, result)