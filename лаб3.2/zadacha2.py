import re
f = [str(x) for x in open('Letters.txt')]
sum = []
for i in range(len(f)):
    sum.append(f[i])
Ball = 0
print('Это игра Эрудит! Введите ваше слово на английском языке..')
print('..в верхнем регистре (например, HELLO): ')
Word = str(input())
for i in range(len(Word)):
    for x in range(len(sum)):
        if Word[i] in sum[x]:
            m = re.findall('\d+', sum[x])
            m = m[0] 
            Ball = Ball + int(m)
print(Ball)
