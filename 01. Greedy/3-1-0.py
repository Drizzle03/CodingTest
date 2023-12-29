# 숫자카드게임 : 개인 풀이
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 행을 하나 선택해 해당 행에서 가장 숫자가 낮은 카드를 뽑아야함

n, m = map(int, input().split())
max = -9999

#입력 및 정렬
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    if(max < a[0]):
        max = a[0]

print(max)