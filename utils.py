import os
import pathlib


class Streamer(object):
    def __init__(self, file_path):
        self.f = open(file_path, "r")
        self.pattern_byte = 0

    def next(self):
        if self.f.tell() == 0:
            line = self.f.readline().replace("\n", "")
            self.pattern_byte = self.f.tell()
        else:
            line = self.f.readline().replace("\n", "")
        return line

    def set_seek(self):
        self.f.seek(self.pattern_byte)

def load_input_data_stream(path):
    '''
    입력 데이터 형식을 스트림 형식으로 제공하는 함수
    :param path: 입력 데이터의 파일 경로
    :return: 순서대로 들어오는 정보인 패턴크기, 텍스트크기, 파일 스트림 객체 반환
    '''
    assert os.path.exists(path), "Please check input path"
    stream = Streamer(path)
    line = stream.next()
    pattern_len, text_len = line.split()
    pattern_len, text_len = int(pattern_len), int(text_len)

    return pattern_len, text_len, stream

def load_input_data(path):
    '''
    입력 데이터 형식을 파싱하고 튜플 형태로 반환하는 함수
    :param path: 입력 데이터의 파일 경로
    :return: 순서대로 들어오는 정보인 패턴크기, 텍스트크기, 패턴에 대한 2차원배열, 텍스트에 대한 2차원 배열을 반환
    '''
    assert os.path.exists(path), "Please check input path"
    with open(path, "r") as f:
        lines = [line.replace("\n", "").strip() for line in f.readlines()]
        pattern_len, text_len = lines[0].split()
        pattern_len, text_len = int(pattern_len), int(text_len)

        patterns = lines[1:1+pattern_len]
        text = lines[1+pattern_len:1+pattern_len+text_len]

    return pattern_len, text_len, patterns, text

def load_output_data(path):
    '''
    출력 데이터 형식을 파싱하고 튜플 형태로 반환하는 함수
    :param path: 출력 데이터의 파일 경로
    :return: 한줄마다 패턴 매칭 결과를 튜플 배열로 만들어 반환
    '''
    assert os.path.exists(path), "Please check output path"
    with open(path, "r") as f:
        lines = [line.replace("\n","").strip().split() for line in f.readlines()]

    return [(int(line[0]), int(line[1])) for line in lines]

def save_output_data(path, result):
    '''
    출력 데이터 형식대로 결과 튜플을 출력해주는 함수
    :param path: 출력 데이터의 파일 경로
    :param result: 매칭된 패턴의 위치 튜플의 배열
    :return: -
    '''
    dirname = os.path.dirname(path)
    pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        for i, j in result:
            f.write(f'{i} {j}\n')

def save_check_data(path, result):
    '''
    Check 데이터 형식대로 구현된 Baker-bird 알고리즘과 Checker program의 결과를 출력하는 함수
    :param path: Check 데이터의 파일 경로
    :param result: Checker 결과
    :return: -
    '''
    dirname = os.path.dirname(path)
    pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        f.write(result)