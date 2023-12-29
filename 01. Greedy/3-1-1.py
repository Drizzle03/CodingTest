#서적 풀이 : min 함수 사용

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) #가장 작은 값 찾고
    result = max(result, min_value) #지금 값과 min값 중 더 큰 거 반환해 저장 

print(result)