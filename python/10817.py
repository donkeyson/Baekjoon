#세 정수 a, b, c
#두 번째로 큰 정수 출력
se = 0
a, b, c = map(int, input().split())
li = []
li.append(a)
li.append(b)
li.append(c)
li.remove(max(li))
li.remove(min(li))
print(li[0])
