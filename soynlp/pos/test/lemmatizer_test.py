# -*- encoding:utf8 -*-
import sys
sys.path.append('../../../')
from soynlp.pos._lemmatizer import Lemmatizer

def main():
    test_roots = {
        '깨닫', '불', '묻', '눋', '겯', '믿', '묻', '뜯', # ㄷ 불규칙
        '구르', '무르', '마르', '누르', '나르', '모르', '이르', # 르 불규칙
        '아니꼽', '우습', '더럽', '아름답', '잡', '뽑', '곱', '돕', # ㅂ 불규칙
        '낫', '긋', '붓', '뭇', '벗', '솟', '치솟', '씻', '손씻', '뺏', # ㅅ 불규칙
        '똥푸', '주', '좀주', '푸', # 우 불규칙
        '끄', '크', '트', # ㅡ 탈락 불규칙
        '삼가', '가', '들어가', # 거라 불규칙
        '돌아오', '오', # 너라 불규칙
        '이르', '푸르', '누르', # 러 불규칙
        '하', # 여 불규칙
        '가', '노랗', '퍼렇', '놀라', # 어미 ㄴ
        '시퍼렇', '파랗',  # ㅎ 불규칙
        '먹',
        '보', '뵈', '뵙', '그렇'
    }

    test_eomis = {
        '',
        '아', '어나다', '어', '워', '웠다', '워서', '왔다', '와주니', '었다', '었어', '았어', '데', 
        '라', '라니까', '너라', '았다', '러', '였다', '았다', '면', '다', '거라', '고', '는', '니'
    }

    testset = [
        ('깨달' ,'아'),
        ('굴' ,'러'),
        ('더러' ,'워서'),
        ('도' ,'왔다'),
        ('부' ,'었다'),
        ('똥퍼' ,''),
        ('퍼' ,''),
        ('줬' ,'어'),
        ('꺼' ,''),
        ('텄' ,'어'),
        ('가' ,'거라'),
        ('돌아오' ,'거라'),
        ('돌아왔' ,'다'),
        ('이르' ,'러'),
        ('파라' ,'면'),
        ('시퍼렜' ,'다'),
        ('파랬' ,'다'),
        ('파래' ,''),
        ('간' ,''),
        ('푸른' ,''),
        ('한' ,''),
        ('이른' ,''),
        ('불', '어'),
        ('부', '어'),
        ('일', '러'),
        ('이르', '니'),
        ('이른', ''),
        ('뵈', '고'),
        ('뵙', '고'),
        ('뵙', '는'),
        ('그래', ''),
    ]
    
    lemmatizer = Lemmatizer(test_roots, test_eomis)
    for l,r in testset:
        print('({}, {}) -> {}'.format(l,r,lemmatizer.lemmatize(l+r)))

if __name__ == '__main__':
    main()