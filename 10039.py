#평균 점수
#총 수강생 5명, 연속으로 입력되는 점수 5개 

#40점 이상은 그대로 40점 미만은 점수 40점 처리

#출력값은 5명 점수의 평균값. 출력은 정수로

arr = []
for _ in range(5):
    a = int(input())
    arr.append(a)
    
sum = 0
for i in arr:
    if i >= 40:
        sum += i
    else:
        sum += 40

avg = sum / 5
print(int(avg))
