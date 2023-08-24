data_list1 = [40,30,10,50,20]
data_list2 = ['B', 'F', 'A', 'D', 'C', 'E']
## 오름차순 정렬 ##
print('정렬 전 =', data_list1)
data_list1.sort()
print('정렬 후 =', data_list1)
print()
print('정렬 전 =', data_list2)
data_list2.sort()
print('정렬 전 =', data_list2)
print()
print()
## 내림차순 정렬 ##
print('정렬 전 =', data_list1)
data_list1.sort(reverse=True)
print('정렬 후 =', data_list1)
print()
print()
print('정렬 전 =', data_list2)
data_list2.sort(reverse=True)
print('정렬 후 =', data_list2, end='\n\n\n')

data_list3 = [200, 100, 300, 400]
print(data_list3)
data_list3.sort()
print(data_list3)
data_list3.reverse()
print(data_list3)