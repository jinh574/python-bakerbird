from aho_corasick import AhoCorasick
from kmp import KMP

class BakerBird(object):
    def __init__(self, stream, pattern_len):
        '''
        Baker-bird 알고리즘 이니셜라이징
        :param patterns: Baker-bird 알고리즘을 실행할 패턴 배열
        '''
        self.ac = AhoCorasick()
        for _ in range(pattern_len):
            line = stream.next()
            self.ac.add_patterns(line)
        self.ac.build()

        self.r = {}
        idx = 1

        stream.set_seek()
        for _ in range(pattern_len):
            row = stream.next()
            if row not in self.r.keys():
                self.r[row] = str(idx)
                idx += 1

        stream.set_seek()
        self.kmp = KMP("".join([str(self.r[stream.next()]) for _ in range(pattern_len)]))

    def __call__(self, stream, text_len):
        '''
        Baker-bird 알고리즘 수행, extra space를 최적화 하기 위해 기존 Aho-corasick으로 만들어 낸 2차원 배열을 KMP를 모두 훑는 방식이 아닌
        Aho-corasick 한줄을 수행 후 패턴 크기만큼의 배열만을 생성 유지하고, KMP를 step별로 계산하는 방식으로 구현
        :param text: 매칭할 텍스트
        :return: 매칭이 일어난 끝 좌표를 튜플 배열 형태로 반환
        '''
        ret = []
        position = [0,] * text_len
        for i in range(text_len):
            row = stream.next()
            row_R = ["0",] * text_len
            for start, end, keyword in self.ac(row):
                row_R[end-1] = self.r[keyword]

            for idx, R in enumerate(row_R):
                position[idx] = self.kmp.step(R, position[idx])
                if position[idx] is len(self.kmp.keyword):
                    ret.append((i, idx))
                    position[idx] = self.kmp.pi[position[idx]-1]
        return ret