name = input('이름 : ')
jumsoo= input('점수는 공백으로 구분해서 세과목:').split()
total = 0
# 함수 미사용
for j in jumsoo:
    total = total + int(j)
ave = total / len(jumsoo)
#함수 사용

print(f'Name kor eng mat total ave')
print(f'{name} {jumsoo[0]} {jumsoo[1]} {jumsoo[2]} {total}  {ave}')