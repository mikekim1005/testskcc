name = input('이름은 ?')
kor = int(input('국어 ?'))
eng = int(input('영어 ?'))
mat = int(input('수학 ?'))
total = kor + eng + mat
ave = total / 3
print('이름  국어  영어  수학  총점  평균')
print(f'{name}  {kor} {eng} {mat}   {total}   {ave}')

