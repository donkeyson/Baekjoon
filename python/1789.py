//자연수 s 입력
//s는 서로 다른 n개의 자연수의 합

s = int(input())
n = 1
while n * (n + 1) / 2 <= s: //수열 공식 활용
  n += 1
print(n - 1)
