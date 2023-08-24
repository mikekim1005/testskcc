import   os
print(os.getcwd())
list1 = ['aaa', 'bbb', 'ccc']
list2 = ['aaa', 'bbb', 'ccc']
list3 = ['aaa', 'bbb', 'ccc']
list4 = ['aaa', 'bbb', 'ccc']
fp = open('file7.txt','w')
fp.writelines(' '.join(list1))
fp.writelines('\n')
fp.writelines(','.join(list2))
fp.writelines('\n')
fp.writelines(':'.join(list3))
fp.writelines('\n')
fp.writelines(';'.join(list4))
fp.writelines('\n')
fp.close()