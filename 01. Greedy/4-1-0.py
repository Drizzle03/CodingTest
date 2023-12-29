#1이 될 때까지 : 개인 풀이
#어떤 수 N이 1이 될 때까지 두 과정 중 1개 택해 진행
# 1. N에서 1을 뺌
# 2. N을 K로 나눔
# 그리디이므로, N을 K로 나눌 수 있을 때 2, 아닐 때 1 사용

n, k = map(int, input().split())
result = 0

while True:
    #종료 조건에 도달했을 때
    if(n <= 1):
        break
    
    #N을 K로 나눌 수 있을 때
    if(n % k == 0):
        n //= k #n을 k로 나눈 몫만큼 k를 곱해 뺌
        result += 1

    else:
        n-=1
        result+=1

print(result)
    