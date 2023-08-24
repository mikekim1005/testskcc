t1 = (1,2,3,4,5)
l1 = [1,2,3,4,5]
# print(type(t1))
# print(len(t1))
# print(t1[0])
# print(t1[4])
# l1[0] = l1[0] + 100
# print(l1[0])

#t1[0] = t1[0] + 200
# print(t1[0] + 200)

a = 100
b = 200
print('a = ', a, 'b = ', b)
# 두 기억장소의 값을 교환하는 전형(일반)적인 알고리즘
# c = a
# a = b
# b = c
## 튜플을 이용한 알고리즘
(a,b) = (b,a)
print('a = ', a, 'b = ', b)
print(t1.index(3))