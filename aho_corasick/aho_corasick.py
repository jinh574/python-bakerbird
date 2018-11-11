from collections import deque

from .node import Node

class AhoCorasick(object):
    def __init__(self):
        '''
        AhoCorasick 이니셜라이징
        '''
        self.head = Node()
        self.head.fail = 0
        self.pattern = set()
        self.idx = 1

        self.aho_corasick = {0: self.head}

    def __call__(self, text):
        '''
        미리 만들어 놓음 Trie를 기반으로 AhoCorasick 알고리즘을 구현
        :param text: 매칭할 텍스트
        :return: 매칭 결과를 시작, 끝, 키워드 튜플 배열로 반환 [(INT start, INT end, STRING keyword), ...]
        '''
        current = self.head

        ret = []
        for idx, char in enumerate(text):
            while True:
                if not current.goto(char) and current.idx is not 0:
                    current = self.aho_corasick[current.fail]
                else:
                    child = current.goto(char)
                    break
            if child:
                current = child
                if child.output:
                    keyword = max(list(child.output), key=len)
                    start = idx - len(keyword) + 1
                    end = start + len(keyword)
                    ret.append((start, end, keyword))
        return ret

    def add_pattern(self, pattern):
        '''
        TRIE에 생성할 패턴을 입력받는 함수
        :param pattern: TRIE를 생성할 패턴
        :return: -
        '''
        self.pattern.add(pattern)
        current = self.head


        for char in pattern:
            if char not in current.children.keys():
                current.children[char] = Node(self.idx, char)
                self.aho_corasick[self.idx] = current.children[char]
                self.idx += 1
            current = current.children[char]
        current.output.add(pattern)

    def add_patterns(self, patterns):
        '''
        배열 형식으로 패턴을 여러개를 한꺼번에 입력받는 함수
        :param patterns: TRIE를 생성할 패턴 배열
        :return: -
        '''
        if type(patterns) is str:
            patterns = patterns.split()
        assert type(patterns) is list, "Please input list or str with space"

        for pattern in patterns:
            self.add_pattern(pattern)

    def _compute_fail_func(self):
        '''
        입력받은 패턴들을 기반으로 failure function을 계산하는 함수
        :return: -
        '''
        queue = deque()

        for node in self.head.children.values():
            queue.append(node)
        while queue:
            target = queue.popleft()
            for node in target.children.values():
                queue.append(node)
                idx = target.fail
                char = node.char
                current = self.aho_corasick[idx]

                while not current.goto(char) and current.idx is not 0:
                    new_idx = current.fail
                    current = self.aho_corasick[new_idx]

                if not current.goto(char):
                    node.fail = current.idx
                else:
                    node.fail = current.goto(char).idx

                node.set_output(self.aho_corasick[node.fail].output)


    def build(self):
        '''
        패턴 입력 후 트리거 함수
        :return: -
        '''
        self._compute_fail_func()


if __name__ == "__main__":
    aho = AhoCorasick()
    aho.add_pattern("hi")
    aho.add_pattern("this")
    aho.build()

    aho("this is my first aho-corasick implemented. and")