# list1 = [10,20,30,40,50]
# total = sum(list1)
# ave = total / len(list1)
# print(total, ave)

# import statistics
# list2 = ['10,20,30,40,50']
# #리스트의 형변환
# list2 = map(int, list2)
# total = sum(list2)
# ave = statistics.mean(list2)
# print(total, ave)


import statistics
list2 = ['10','20','30','40','50']
print(list2)
#리스트의 형변환(for문 사용)
# i = 0
# for data in list2:
#     list2[i] = int(data)
#     i = i + 1

#리스트의 ㅣ형변환(컴프리헨션 사용)
[ int(data)  for  data  in  list2 ]
print(list2)

#리스트의 형변환
list2 = map(int, list2)
print(list2)
# total = sum(list2)
# ave = statistics.mean(list2)
# print(total, ave)