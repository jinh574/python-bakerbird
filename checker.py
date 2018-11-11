import argparse

from utils import load_input_data, load_output_data, save_output_data, save_check_data

# 실행 매개변수 Parsing
parser = argparse.ArgumentParser(description="Homework checker program")
parser.add_argument("input", type=str,
                    help="Input txt file path")
parser.add_argument("output", type=str,
                    help="Output txt file path")
parser.add_argument("check", type=str,
                    help="Check status txt file path")
args = parser.parse_args()


def checker_numpy(pattern_len, text_len, patterns, text):
    '''
    Checker program core code.
    패턴 2차원 배열이 Window sliding 형식으로 텍스트를 1칸씩 시프트하면서 순차 검색 후 모든 문자가 같으면 해당 position을 반환

    :param pattern_len: 패턴 매트릭스의 크기
    :param text_len: 텍스트 매트릭스의 크기
    :param patterns: 패턴 2차원 배열
    :param text:: 텍스트 2차원 배열
    :return: 텍스트 내 매칭되는 모든 매트릭스의 postion을 튜플 형식으로 반환
    '''
    import numpy as np

    ret = []

    pattern_np, text_np = np.array([list(v) for v in patterns]), np.array([list(v) for v in text])
    for i in range(text_len - pattern_len + 1):
        for j in range(text_len - pattern_len + 1):
            mask = text_np[i:i + pattern_len, j:j + pattern_len] == pattern_np
            if mask.all():
                ret.append((i + pattern_len - 1, j + pattern_len - 1))

    return ret

def checker_naive(pattern_len, text_len, patterns, text):
    '''
    패턴 2차원 배열이 Window sliding 형식으로 텍스트를 1칸씩 시프트하면서 순차 검색 후 모든 문자가 같으면 해당 position을 반환

    :param pattern_len: 패턴 매트릭스의 크기
    :param text_len: 텍스트 매트릭스의 크기
    :param patterns: 패턴 2차원 배열
    :param text:: 텍스트 2차원 배열
    :return: 텍스트 내 매칭되는 모든 매트릭스의 postion을 튜플 형식으로 반환
    '''
    ret = []

    pattern_arr, text_arr = [list(v) for v in patterns], [list(v) for v in text]
    for i in range(text_len - pattern_len + 1):
        for j in range(text_len - pattern_len + 1):
            mask = [e[j:j + pattern_len]for e in text_arr[i:i + pattern_len]] == pattern_arr
            if mask:
                ret.append((i + pattern_len - 1, j + pattern_len - 1))

    return ret


if __name__ == "__main__":
    data = load_input_data(args.input)
    outputs = load_output_data(args.output)

    check_result = checker_naive(*data)
    print(check_result)

    if check_result == outputs:
        save_check_data(args.check, "yes")
    else:
        save_check_data(args.check, "no")