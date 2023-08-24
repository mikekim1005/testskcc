data = """
kim 220101-3000001
lee 220102-4000002
jang 220103-3000003
ha 220104-4000004
"""

result = []
for line in data.split('/n'):
    word_result = []
    for word in line.split(' '):
            if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
                word = word[:6] + '-' + "*******"
            word_result.append(word)
    result.append(' '.join(word_result))

print('\n'.join(result))