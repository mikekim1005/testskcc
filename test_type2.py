list2 = [10,20,30,40,50]
jumsoo = list(map(int, jumsoo))
total = sum(jumsoo)
ave = statistics.mean(jumsoo)
print(f'Name kor  eng  mat  total  ave')
print(f'{name} {jumsoo[0]} {jumsoo[1]} {jumsoo[2]} {total} {ave}')
