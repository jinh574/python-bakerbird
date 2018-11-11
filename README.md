# python-bakerbird
Implemented Baker-Bird algorithm

# ENVIRONMENT
Python version: 3.6.5
Environment OS: Ubuntu 14.04

# PACKAGE
example
* example_running01.txt
* example_running02.txt

aho_corasick
* aho_corasick.py       : Aho-corasick 알고리즘 구현 파일
* node.py               : Trie 트리 생성을 위한 Node 구현 파일

baker_bird
* baker_bird.py         : Baker-bird 알고리즘 구현 파일

kmp
* kmp.py                : KMP 알고리즘 구현 파일

checker.py                  : Checker 프로그램 구현 파일(구현에 상관없이 완벽하게 만들어도 된다는 조교님의 말씀에 numpy를 이용하여 윈도우 슬라이딩 형식으로 구현)
main.py                     : Baker-bird 알고리즘 실행 스크립트
utils.py                    : 입력, 출력 파일 파싱 관련 유틸리티성 함수 구현 파일

# HOW TO USE
python main.py input.txt output.txt
python checker.py input.txt output.txt check.txt
