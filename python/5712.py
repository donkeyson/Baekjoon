//상근이의 남자 친구 수
//여자 친구 수
//친구는 총 몇명?
//여러 개의 테스트 케이스
//마지막은 0 0

a, b = map(int, input().split())
while not (a == 0 and b == 0):
    print(a+b)
    a, b = map(int, input().split())
