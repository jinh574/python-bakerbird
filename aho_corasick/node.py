class Node(object):
    '''
    Trie를 구현하기 위한 Node class
    '''
    def __init__(self, idx=0, char=None):
        '''
        Node 이니셜라이징
        :param idx: 노드의 인덱스
        :param char: 해당 노드가 표현하는 문자
        '''
        self.idx = idx
        self.char = char;
        self.children = {}
        self.fail = 0
        self.output = set()

    def goto(self, char):
        '''
        현재 노드가 문자가 들어왔을 때 어떠한 노드로 향해야하는지 반환하는 함수
        :param char: 현재 노드 다음으로 들어올 문자
        :return: 해당하는 문자로 타고 들어갈 수 있는 노드 또는 없음
        '''
        if char in self.children.keys():
            return self.children[char]
        else:
            return None

    def set_output(self, output_set):
        '''
        마지막에 계산될 output keyword set 추가 함수
        :param output_set: 추가하기 위한 output_set
        :return: -
        '''
        self.output = self.output ^ output_set

    def __repr__(self):
        return "({}, {}, {}, {})".format(self.idx, self.char, list(self.children.keys()), self.fail)