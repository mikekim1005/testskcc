# 단 제목 출력
# for dan in range(2,10):
#     print(f' == {dan}단  == ', end='')
# print()
#

#구구단 결과 출력
# 2 x 1 = 2,  3 x 1 = 3  ~~~~~~ 9 x 1 = 9
# 2 x 2 = 4,  3 x 2 = 6  ~~~~~~ 9 x 2 = 18
# for i  in range(1,10):
#     for j in reversed(range(1,10)):
#         print(f'{j} x {i} = {(j*i):2} ', end='')
#     print()
# print(f'구구단 출력 완료')

# for i  in range(9, 0, -1):
#     for j in (range(9, 1, -1)):
#         print(f'{j} x {i}  = {(j*i):2} ', end=' ')
#     print()
# print(f'구구단 출력 완료')

# ticker = 'btc krw'
# ticker = ticker.upper()
# print(ticker)
#
# ticker = "BTC_KRW"
# ticker = ticker.lower()
# print(ticker)

# a = 'hello'
# a = a.capitalize()
# print(a)

# filename = '보고서.xlsx'
# print(filename.endswith('xlsx'))

# filename = '2020_보고서.xlsx'
# print(filename.startswith('2020'))

# a = 'hello world'
# print(a.split())

# date = '2020-05-01'
# print(date.split('-'))

# data = '039490      '
# print(data.rstrip())

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.append('배트맨')
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.insert(1, '배트맨')
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.remove('스플릿')
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '배트맨', '스플릿', '럭키']
# del movie_rank[1]
# del movie_rank[2]
# print(movie_rank)

# lang1 = ['C', 'C++', 'JAVA']
# lang2 = ['Python', 'Go', 'C#']
# langs = lang1 + lang2
# print(langs)

# nums = [1,2,3,4,5,6,7]
# print('max: ', max(nums))
# print('min: ', min(nums))

# nums = [1,2,3,4,5,6,7]
# print(sum(nums))

# cook = ['피자','김밥','만두','양념치킨','족발','김치만두','쫄면','소세지','팥빙수']
# print(len(cook))

# nums = [1,2,3,4,5]
# average = sum(nums) / len(nums)
# print(average)

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[::-1])
















