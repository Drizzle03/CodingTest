#서적 풀이 제공
n, m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    #가장 큰 수 덧셈
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1 #덧셈횟수 차감

    # 종료 조건
    if m==0:
        break
    result += second
    m -= 1
print(result)