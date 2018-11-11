class KMP(object):
    def __init__(self, keyword):
        '''
        KMP 알고리즘 이니셜 함수로 string match에 사용될 keyword를 입력받고 Pi 배열을 생성
        :param keyword: 패턴으로 사용될 키워드
        '''
        self.keyword = keyword
        self.pi = self._generate_pi(keyword)

    def __call__(self, text):
        '''
        String match를 할 텍스트를 입력받고 결과를 반환
        :param text: 매칭할 텍스트
        :return: 매칭이 일어난 시작, 끝 위치와 매칭된 키워드의 튜플 배열, [(INT start, INT end, STRING keyword), ...]
        '''
        keyword_len = len(self.keyword)

        ret = []
        position = 0
        for idx in range(len(text)):
            while position > 0 and text[idx] != self.keyword[position]:
                position = self.pi[position-1]
            if text[idx] == self.keyword[position]:
                if position == len(self.keyword) - 1:
                    start = idx - position + 1
                    end = start + keyword_len
                    ret.append((start, end, self.keyword))
                    position = self.pi[position]
                else:
                    position += 1
        return ret

    def step(self, char, position):
        '''
        기존 KMP 알고리즘을 이용하여 한단계씩 나누어 계산을 하기 위해 구현된 함수
        :param char: 매칭을 확인할 문자
        :param position: 지금까지 진행된 매칭 위치
        :return: 매칭 결과로 움직여야할 위치 (true=다음위치, false면 failue Pi위치)
        '''
        while position > 0 and char != self.keyword[position]:
            position = self.pi[position-1]
        if char == self.keyword[position]:
            position += 1

        return position


    def _generate_pi(self, keyword):
        '''
        키워드를 입력받아 Pi 배열을 생성하는 함수
        :param keyword: Pi 배열을 생성할 키워드
        :return: Pi 배열
        '''
        pi = [0, ] * len(keyword)

        position = 0
        for idx in range(1, len(keyword)):
            while position > 0 and keyword[idx] != keyword[position]:
                position = pi[position - 1]
            if keyword[idx] == keyword[position]:
                position += 1
                pi[idx] = position

        return pi


if __name__ == "__main__":
    kmp = KMP("jeeseung")
    print(kmp("Hi my name is jeeseung han. jeeseung!"))