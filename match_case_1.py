# jumsu = 35
# mok = jumsu // 10
# match mok:
#     case 9:
#         print('A')
#     case 8:
#         print('B')
#     case 7:
#         print('C')
#     case 6:
#         print('D')
#     case default:
#         print('F')
# print('학점 계산 완료')
#
Key_list = [9, 8, 7, 6]
Value_list = ["A", "B", "C", "D"]

hak_table = dict(zip(Key_list, Value_list))

score = 95
mok = score // 10
result = hak_table.get(mok, "F")
print(f"당신의 성적은 {result} 입니다")

