# fp = open(r'C:/python/test.txt', 'wt')
# for i  in range(16,21):
#     output_data = f'{i} 번째 내용입니다. \n'
#     fp.write(output_data)
#
# fp.close()
# print(f'파일을 잘 닫았습니다')

fp = open(r'C:/python/test.txt', 'at')
for i  in range(16,21):
    output_data = f'{i} 번째 내용입니다. \n'
    fp.write(output_data)

fp.close()
print(f'파일을 잘 닫았습니다')
